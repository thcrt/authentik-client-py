# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.10.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_client.models.auth_mode_enum import AuthModeEnum
from authentik_client.models.protocol_enum import ProtocolEnum
from authentik_client.models.rac_provider import RACProvider
from typing import Optional, Set
from typing_extensions import Self

class Endpoint(BaseModel):
    """
    Endpoint Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    provider: StrictInt
    provider_obj: RACProvider
    protocol: ProtocolEnum
    host: StrictStr
    settings: Optional[Any] = None
    property_mappings: Optional[List[StrictStr]] = None
    auth_mode: AuthModeEnum
    launch_url: Optional[StrictStr] = Field(description="Build actual launch URL (the provider itself does not have one, just individual endpoints)")
    maximum_connections: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    __properties: ClassVar[List[str]] = ["pk", "name", "provider", "provider_obj", "protocol", "host", "settings", "property_mappings", "auth_mode", "launch_url", "maximum_connections"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Endpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "provider_obj",
            "launch_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of provider_obj
        if self.provider_obj:
            _dict['provider_obj'] = self.provider_obj.to_dict()
        # set to None if settings (nullable) is None
        # and model_fields_set contains the field
        if self.settings is None and "settings" in self.model_fields_set:
            _dict['settings'] = None

        # set to None if launch_url (nullable) is None
        # and model_fields_set contains the field
        if self.launch_url is None and "launch_url" in self.model_fields_set:
            _dict['launch_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Endpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "provider": obj.get("provider"),
            "provider_obj": RACProvider.from_dict(obj["provider_obj"]) if obj.get("provider_obj") is not None else None,
            "protocol": obj.get("protocol"),
            "host": obj.get("host"),
            "settings": obj.get("settings"),
            "property_mappings": obj.get("property_mappings"),
            "auth_mode": obj.get("auth_mode"),
            "launch_url": obj.get("launch_url"),
            "maximum_connections": obj.get("maximum_connections")
        })
        return _obj


