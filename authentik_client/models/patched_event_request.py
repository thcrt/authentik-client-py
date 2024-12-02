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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_client.models.event_actions import EventActions
from typing import Optional, Set
from typing_extensions import Self

class PatchedEventRequest(BaseModel):
    """
    Event Serializer
    """ # noqa: E501
    user: Optional[Any] = None
    action: Optional[EventActions] = None
    app: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    context: Optional[Any] = None
    client_ip: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    expires: Optional[datetime] = None
    brand: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["user", "action", "app", "context", "client_ip", "expires", "brand"]

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
        """Create an instance of PatchedEventRequest from a JSON string"""
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
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if context (nullable) is None
        # and model_fields_set contains the field
        if self.context is None and "context" in self.model_fields_set:
            _dict['context'] = None

        # set to None if client_ip (nullable) is None
        # and model_fields_set contains the field
        if self.client_ip is None and "client_ip" in self.model_fields_set:
            _dict['client_ip'] = None

        # set to None if brand (nullable) is None
        # and model_fields_set contains the field
        if self.brand is None and "brand" in self.model_fields_set:
            _dict['brand'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedEventRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "user": obj.get("user"),
            "action": obj.get("action"),
            "app": obj.get("app"),
            "context": obj.get("context"),
            "client_ip": obj.get("client_ip"),
            "expires": obj.get("expires"),
            "brand": obj.get("brand")
        })
        return _obj


