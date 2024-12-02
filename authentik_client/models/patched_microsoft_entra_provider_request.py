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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_client.models.outgoing_sync_delete_action import OutgoingSyncDeleteAction
from typing import Optional, Set
from typing_extensions import Self

class PatchedMicrosoftEntraProviderRequest(BaseModel):
    """
    MicrosoftEntraProvider Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    property_mappings: Optional[List[StrictStr]] = None
    property_mappings_group: Optional[List[StrictStr]] = Field(default=None, description="Property mappings used for group creation/updating.")
    client_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    client_secret: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    tenant_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    exclude_users_service_account: Optional[StrictBool] = None
    filter_group: Optional[StrictStr] = None
    user_delete_action: Optional[OutgoingSyncDeleteAction] = None
    group_delete_action: Optional[OutgoingSyncDeleteAction] = None
    __properties: ClassVar[List[str]] = ["name", "property_mappings", "property_mappings_group", "client_id", "client_secret", "tenant_id", "exclude_users_service_account", "filter_group", "user_delete_action", "group_delete_action"]

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
        """Create an instance of PatchedMicrosoftEntraProviderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if filter_group (nullable) is None
        # and model_fields_set contains the field
        if self.filter_group is None and "filter_group" in self.model_fields_set:
            _dict['filter_group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedMicrosoftEntraProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "property_mappings": obj.get("property_mappings"),
            "property_mappings_group": obj.get("property_mappings_group"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "tenant_id": obj.get("tenant_id"),
            "exclude_users_service_account": obj.get("exclude_users_service_account"),
            "filter_group": obj.get("filter_group"),
            "user_delete_action": obj.get("user_delete_action"),
            "group_delete_action": obj.get("group_delete_action")
        })
        return _obj


