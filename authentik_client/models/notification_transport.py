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
from authentik_client.models.notification_transport_mode_enum import NotificationTransportModeEnum
from typing import Optional, Set
from typing_extensions import Self

class NotificationTransport(BaseModel):
    """
    NotificationTransport Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    mode: Optional[NotificationTransportModeEnum] = None
    mode_verbose: StrictStr = Field(description="Return selected mode with a UI Label")
    webhook_url: Optional[StrictStr] = None
    webhook_mapping: Optional[StrictStr] = None
    send_once: Optional[StrictBool] = Field(default=None, description="Only send notification once, for example when sending a webhook into a chat channel.")
    __properties: ClassVar[List[str]] = ["pk", "name", "mode", "mode_verbose", "webhook_url", "webhook_mapping", "send_once"]

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
        """Create an instance of NotificationTransport from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "pk",
            "mode_verbose",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if webhook_mapping (nullable) is None
        # and model_fields_set contains the field
        if self.webhook_mapping is None and "webhook_mapping" in self.model_fields_set:
            _dict['webhook_mapping'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationTransport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "mode": obj.get("mode"),
            "mode_verbose": obj.get("mode_verbose"),
            "webhook_url": obj.get("webhook_url"),
            "webhook_mapping": obj.get("webhook_mapping"),
            "send_once": obj.get("send_once")
        })
        return _obj


