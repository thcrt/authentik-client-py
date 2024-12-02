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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_client.models.outgoing_sync_delete_action import OutgoingSyncDeleteAction
from typing import Optional, Set
from typing_extensions import Self

class GoogleWorkspaceProvider(BaseModel):
    """
    GoogleWorkspaceProvider Serializer
    """ # noqa: E501
    pk: StrictInt
    name: StrictStr
    property_mappings: Optional[List[StrictStr]] = None
    property_mappings_group: Optional[List[StrictStr]] = Field(default=None, description="Property mappings used for group creation/updating.")
    component: StrictStr = Field(description="Get object component so that we know how to edit the object")
    assigned_backchannel_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_backchannel_application_name: StrictStr = Field(description="Application's display Name.")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    delegated_subject: Annotated[str, Field(strict=True, max_length=254)]
    credentials: Optional[Any]
    scopes: Optional[StrictStr] = None
    exclude_users_service_account: Optional[StrictBool] = None
    filter_group: Optional[StrictStr] = None
    user_delete_action: Optional[OutgoingSyncDeleteAction] = None
    group_delete_action: Optional[OutgoingSyncDeleteAction] = None
    default_group_email_domain: StrictStr
    __properties: ClassVar[List[str]] = ["pk", "name", "property_mappings", "property_mappings_group", "component", "assigned_backchannel_application_slug", "assigned_backchannel_application_name", "verbose_name", "verbose_name_plural", "meta_model_name", "delegated_subject", "credentials", "scopes", "exclude_users_service_account", "filter_group", "user_delete_action", "group_delete_action", "default_group_email_domain"]

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
        """Create an instance of GoogleWorkspaceProvider from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "component",
            "assigned_backchannel_application_slug",
            "assigned_backchannel_application_name",
            "verbose_name",
            "verbose_name_plural",
            "meta_model_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if credentials (nullable) is None
        # and model_fields_set contains the field
        if self.credentials is None and "credentials" in self.model_fields_set:
            _dict['credentials'] = None

        # set to None if filter_group (nullable) is None
        # and model_fields_set contains the field
        if self.filter_group is None and "filter_group" in self.model_fields_set:
            _dict['filter_group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleWorkspaceProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "property_mappings": obj.get("property_mappings"),
            "property_mappings_group": obj.get("property_mappings_group"),
            "component": obj.get("component"),
            "assigned_backchannel_application_slug": obj.get("assigned_backchannel_application_slug"),
            "assigned_backchannel_application_name": obj.get("assigned_backchannel_application_name"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "delegated_subject": obj.get("delegated_subject"),
            "credentials": obj.get("credentials"),
            "scopes": obj.get("scopes"),
            "exclude_users_service_account": obj.get("exclude_users_service_account"),
            "filter_group": obj.get("filter_group"),
            "user_delete_action": obj.get("user_delete_action"),
            "group_delete_action": obj.get("group_delete_action"),
            "default_group_email_domain": obj.get("default_group_email_domain")
        })
        return _obj


