from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="UploadSyncedResourceRequest")


@_attrs_define
class UploadSyncedResourceRequest:
    """
    Attributes:
        name (str):
        data (File):
        knowledge_id (UUID):
        parent_id (Union[None, UUID, Unset]):
        auto_process (Union[None, Unset, bool]):
        wait_for_completion (Union[None, Unset, bool]):
    """

    name: str
    data: File
    knowledge_id: UUID
    parent_id: Union[None, UUID, Unset] = UNSET
    auto_process: Union[None, Unset, bool] = UNSET
    wait_for_completion: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data = self.data.to_tuple()

        knowledge_id = str(self.knowledge_id)

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        auto_process: Union[None, Unset, bool]
        if isinstance(self.auto_process, Unset):
            auto_process = UNSET
        else:
            auto_process = self.auto_process

        wait_for_completion: Union[None, Unset, bool]
        if isinstance(self.wait_for_completion, Unset):
            wait_for_completion = UNSET
        else:
            wait_for_completion = self.wait_for_completion

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "data": data,
                "knowledgeId": knowledge_id,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if auto_process is not UNSET:
            field_dict["autoProcess"] = auto_process
        if wait_for_completion is not UNSET:
            field_dict["waitForCompletion"] = wait_for_completion

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("data", self.data.to_tuple()))

        files.append(("knowledgeId", (None, str(self.knowledge_id), "text/plain")))

        if not isinstance(self.parent_id, Unset):
            if isinstance(self.parent_id, UUID):
                files.append(("parentId", (None, str(self.parent_id), "text/plain")))
            else:
                files.append(("parentId", (None, str(self.parent_id).encode(), "text/plain")))

        if not isinstance(self.auto_process, Unset):
            if isinstance(self.auto_process, bool):
                files.append(("autoProcess", (None, str(self.auto_process).encode(), "text/plain")))
            else:
                files.append(("autoProcess", (None, str(self.auto_process).encode(), "text/plain")))

        if not isinstance(self.wait_for_completion, Unset):
            if isinstance(self.wait_for_completion, bool):
                files.append(("waitForCompletion", (None, str(self.wait_for_completion).encode(), "text/plain")))
            else:
                files.append(("waitForCompletion", (None, str(self.wait_for_completion).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        data = File(payload=BytesIO(d.pop("data")))

        knowledge_id = UUID(d.pop("knowledgeId"))

        def _parse_parent_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_auto_process(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        auto_process = _parse_auto_process(d.pop("autoProcess", UNSET))

        def _parse_wait_for_completion(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        wait_for_completion = _parse_wait_for_completion(d.pop("waitForCompletion", UNSET))

        upload_synced_resource_request = cls(
            name=name,
            data=data,
            knowledge_id=knowledge_id,
            parent_id=parent_id,
            auto_process=auto_process,
            wait_for_completion=wait_for_completion,
        )

        return upload_synced_resource_request
