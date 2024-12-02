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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class GroupMember(BaseModel):
    """
    Stripped down user serializer to show relevant users for groups
    """ # noqa: E501
    pk: StrictInt
    username: Annotated[str, Field(strict=True, max_length=150)] = Field(description="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    name: StrictStr = Field(description="User's display name.")
    is_active: Optional[StrictBool] = Field(default=None, description="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.")
    last_login: Optional[datetime] = None
    email: Optional[Annotated[str, Field(strict=True, max_length=254)]] = None
    attributes: Optional[Dict[str, Any]] = None
    uid: StrictStr
    __properties: ClassVar[List[str]] = ["pk", "username", "name", "is_active", "last_login", "email", "attributes", "uid"]

    @field_validator('username')
    def username_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\w.@+-]+$", value):
            raise ValueError(r"must validate the regular expression /^[\w.@+-]+$/")
        return value

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
        """Create an instance of GroupMember from a JSON string"""
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
            "uid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if last_login (nullable) is None
        # and model_fields_set contains the field
        if self.last_login is None and "last_login" in self.model_fields_set:
            _dict['last_login'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GroupMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "username": obj.get("username"),
            "name": obj.get("name"),
            "is_active": obj.get("is_active"),
            "last_login": obj.get("last_login"),
            "email": obj.get("email"),
            "attributes": obj.get("attributes"),
            "uid": obj.get("uid")
        })
        return _obj


