from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_configuration import ContextConfiguration
    from ..models.update_user_request_context_type_0 import UpdateUserRequestContextType0


T = TypeVar("T", bound="UpdateUserRequest")


@_attrs_define
class UpdateUserRequest:
    """
    Attributes:
        family_name (str):
        given_name (str):
        context (Union['UpdateUserRequestContextType0', None, Unset]):
        context_configuration (Union[Unset, ContextConfiguration]):
    """

    family_name: str
    given_name: str
    context: Union["UpdateUserRequestContextType0", None, Unset] = UNSET
    context_configuration: Union[Unset, "ContextConfiguration"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_user_request_context_type_0 import UpdateUserRequestContextType0

        family_name = self.family_name

        given_name = self.given_name

        context: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, UpdateUserRequestContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        context_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_configuration, Unset):
            context_configuration = self.context_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "familyName": family_name,
                "givenName": given_name,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if context_configuration is not UNSET:
            field_dict["contextConfiguration"] = context_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_configuration import ContextConfiguration
        from ..models.update_user_request_context_type_0 import UpdateUserRequestContextType0

        d = dict(src_dict)
        family_name = d.pop("familyName")

        given_name = d.pop("givenName")

        def _parse_context(data: object) -> Union["UpdateUserRequestContextType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = UpdateUserRequestContextType0.from_dict(data)

                return context_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateUserRequestContextType0", None, Unset], data)

        context = _parse_context(d.pop("context", UNSET))

        _context_configuration = d.pop("contextConfiguration", UNSET)
        context_configuration: Union[Unset, ContextConfiguration]
        if isinstance(_context_configuration, Unset):
            context_configuration = UNSET
        else:
            context_configuration = ContextConfiguration.from_dict(_context_configuration)

        update_user_request = cls(
            family_name=family_name,
            given_name=given_name,
            context=context,
            context_configuration=context_configuration,
        )

        return update_user_request
