#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "docling==2.42.2",
#     "rational-client",
#     "torch==2.7.1+cpu",
# ]
#
# [[tool.uv.index]]
# name = "pytorch-cpu"
# url = "https://download.pytorch.org/whl/cpu"
# explicit = true
#
# [tool.uv.sources]
# torch = { index = "pytorch-cpu" }
# torchvision = { index = "pytorch-cpu" }
# ///

# https://www.reddit.com/r/learnpython/comments/1l53buq/discussion_using_vscode_with_pep_723_script/
# VIRTUAL_ENV=.venv uv sync --script myscript.py --active
import os
import tempfile
from io import BytesIO

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

from rational_client.core import (
    AnnotationType,
    BboxSelector,
    File,
    Knowledge,
    SyncedResource,
)
from rational_client.utils import run


def serialize_bbox(page_height, bbox):
    """
    Serialize a bounding box to a dictionary with relative top-left coordinates.
    """
    if bbox is None:
        return None
    _bbox = bbox.to_top_left_origin(page_height)
    return {
        "left": _bbox.l,
        "top": _bbox.t,
        "right": _bbox.r,
        "bottom": _bbox.b,
    }


def process(document: SyncedResource, options: dict):
    content = document.get_data()

    # Pipeline options for PDF conversion
    pipeline_options = PdfPipelineOptions(
        images_scale=options.get("docling:images_scale", 1.0),
        generate_picture_images=options.get("docling:generate_picture_images", True),
        do_table_structure=options.get("docling:do_table_structure", True),
        do_ocr=options.get("docling:do_ocr", False),
        do_code_enrichment=options.get("docling:do_code_enrichment", False),
        do_formula_enrichment=options.get("docling:do_formula_enrichment", False),
        do_picture_description=options.get("docling:do_picture_description", False),
    )

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )

    # Extract the original file extension
    filename = document.name
    _, ext = os.path.splitext(filename)
    # Write to a temporary file with the same extension
    with tempfile.NamedTemporaryFile(suffix=ext, delete=True) as tmp:
        tmp.write(content)
        tmp.flush()
        tmp_path = tmp.name
        result = converter.convert(tmp_path)

        # Extract pictures
        docling_doc = result.document
        pictures = docling_doc.pictures

        knowledge = Knowledge(document.knowledge_id)
        resource = knowledge.create_resource(
            name=document.name,
            synced_resource_id=document.id,
        )

        for idx, pic in enumerate(pictures):
            # Get image bytes from PictureItem
            img_bytes = None
            if pic.image and pic.image.pil_image:
                buf = BytesIO()
                pic.image.pil_image.save(buf, format="PNG")
                img_bytes = buf.getvalue()
            if not img_bytes:
                continue
            img_name = f"{os.path.splitext(filename)[0]}_picture_{idx + 1}.png"
            img_file = BytesIO(img_bytes)
            img_file.name = img_name
            pic_synced_resource = knowledge.upload_synced_resource(
                name=img_name,
                contents=File(img_file, file_name=img_name, mime_type="image/png"),
                parent_id=document.id,
            )

            # Get page and bbox from provenance
            page_no = None
            bbox = None
            if pic.prov and len(pic.prov) > 0:
                page_no = pic.prov[0].page_no
                bbox = pic.prov[0].bbox
                # Adjust bbox to top-left origin
                page_height = docling_doc.pages[page_no].size.height
                bbox = serialize_bbox(page_height, bbox)

            # Create annotation in the original resource
            resource.add_annotation(
                annotation_type=AnnotationType.IMAGE,
                selector=BboxSelector(
                    kind="bbox",
                    page=page_no,
                    xmin=bbox["left"],
                    ymin=bbox["top"],
                    xmax=bbox["right"],
                    ymax=bbox["bottom"],
                )
                if bbox
                else None,
                content=f"Picture extracted to {pic_synced_resource.id}",
                data={
                    "page": page_no,
                    "bbox": bbox,
                    "notes": f"Picture extracted to {pic_synced_resource.id}",
                },
                generated_resource_id=pic_synced_resource.id,
            )

        # Return the markdown (optional)
        markdown = docling_doc.export_to_markdown()
        return {str(resource.resource_id): markdown}


run(process)
