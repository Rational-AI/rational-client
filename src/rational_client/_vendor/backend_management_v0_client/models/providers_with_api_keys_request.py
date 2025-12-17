from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.providers_with_api_keys_request_provider_api_keys import ProvidersWithApiKeysRequestProviderApiKeys


T = TypeVar("T", bound="ProvidersWithApiKeysRequest")


@_attrs_define
class ProvidersWithApiKeysRequest:
    """
    Attributes:
        provider_api_keys (ProvidersWithApiKeysRequestProviderApiKeys):
    """

    provider_api_keys: "ProvidersWithApiKeysRequestProviderApiKeys"

    def to_dict(self) -> dict[str, Any]:
        provider_api_keys = self.provider_api_keys.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "providerApiKeys": provider_api_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.providers_with_api_keys_request_provider_api_keys import (
            ProvidersWithApiKeysRequestProviderApiKeys,
        )

        d = dict(src_dict)
        provider_api_keys = ProvidersWithApiKeysRequestProviderApiKeys.from_dict(d.pop("providerApiKeys"))

        providers_with_api_keys_request = cls(
            provider_api_keys=provider_api_keys,
        )

        return providers_with_api_keys_request
