#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#     "pymupdf-layout",
#     "pymupdf4llm",
#     "rational-client",
# ]
# ///
import os
from io import BytesIO

import fitz  # PyMuPDF

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
    # PyMuPDF bbox: [x0, y0, x1, y1] (top-left origin)
    return {
        "left": bbox[0],
        "top": bbox[1],
        "right": bbox[2],
        "bottom": bbox[3],
    }


def process(document: SyncedResource, options: dict):
    content = document.get_data()

    filename = document.name
    pdf_bytes = BytesIO(content)
    doc = fitz.open(stream=pdf_bytes, filetype="pdf", filename=filename)

    knowledge = Knowledge(document.knowledge_id)
    resource = knowledge.create_resource(
        name=document.name,
        synced_resource_id=document.id,
    )
    image_idx = 1

    for page_no in range(len(doc)):
        page = doc[page_no]
        img_list = page.get_images(full=True)
        for img in img_list:
            xref = img[0]
            img_name_in_pdf = img[7]  # image name, e.g., 'Im1'
            bbox = page.get_image_bbox(img_name_in_pdf)  # Use image name, not xref
            pix = fitz.Pixmap(doc, xref)
            # Convert to RGB if not RGB or grayscale
            if pix.n > 4 or (pix.colorspace is None or pix.colorspace.name not in ["RGB", "GRAY"]):
                try:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                except Exception:
                    continue  # Skip unsupported images
            try:
                img_bytes = pix.tobytes("png")
            except Exception:
                continue  # Skip images that can't be converted
            img_name = f"{os.path.splitext(filename)[0]}_picture_{image_idx}.png"
            img_file = BytesIO(img_bytes)
            img_file.name = img_name
            pic_synced_resource = knowledge.upload_synced_resource(
                name=img_name,
                contents=File(img_file, file_name=img_name, mime_type="image/png"),
                parent_id=document.id,
            )
            page_height = page.rect.height
            bbox_dict = serialize_bbox(page_height, bbox)
            resource.add_annotation(
                annotation_type=AnnotationType.IMAGE,
                selector=BboxSelector(
                    kind="bbox",
                    page=page_no,
                    xmin=bbox_dict["left"],
                    ymin=bbox_dict["top"],
                    xmax=bbox_dict["right"],
                    ymax=bbox_dict["bottom"],
                )
                if bbox
                else None,
                content=f"Picture extracted to {pic_synced_resource.id}",
                data={
                    "page": page_no,
                    "bbox": bbox_dict,
                    "notes": f"Picture extracted to resource {pic_synced_resource.id}",
                },
                generated_resource_id=pic_synced_resource.id,
            )
            image_idx += 1

    # Export markdown using pymupdf4llm (if available)
    import pymupdf4llm

    markdown = pymupdf4llm.to_markdown(doc)
    return {str(resource.resource_id): markdown}


run(process)
