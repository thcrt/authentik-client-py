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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_client.models.authentication_enum import AuthenticationEnum
from authentik_client.models.denied_action_enum import DeniedActionEnum
from authentik_client.models.flow_designation_enum import FlowDesignationEnum
from authentik_client.models.flow_layout_enum import FlowLayoutEnum
from authentik_client.models.policy_engine_mode import PolicyEngineMode
from typing import Optional, Set
from typing_extensions import Self

class PatchedFlowRequest(BaseModel):
    """
    Flow Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    slug: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=50)]] = Field(default=None, description="Visible in the URL.")
    title: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Shown as the Title in Flow pages.")
    designation: Optional[FlowDesignationEnum] = Field(default=None, description="Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik.")
    policy_engine_mode: Optional[PolicyEngineMode] = None
    compatibility_mode: Optional[StrictBool] = Field(default=None, description="Enable compatibility mode, increases compatibility with password managers on mobile devices.")
    layout: Optional[FlowLayoutEnum] = None
    denied_action: Optional[DeniedActionEnum] = Field(default=None, description="Configure what should happen when a flow denies access to a user.")
    authentication: Optional[AuthenticationEnum] = Field(default=None, description="Required level of authentication and authorization to access a flow.")
    __properties: ClassVar[List[str]] = ["name", "slug", "title", "designation", "policy_engine_mode", "compatibility_mode", "layout", "denied_action", "authentication"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
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
        """Create an instance of PatchedFlowRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedFlowRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "title": obj.get("title"),
            "designation": obj.get("designation"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "compatibility_mode": obj.get("compatibility_mode"),
            "layout": obj.get("layout"),
            "denied_action": obj.get("denied_action"),
            "authentication": obj.get("authentication")
        })
        return _obj


