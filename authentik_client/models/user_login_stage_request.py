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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_client.models.flow_set_request import FlowSetRequest
from authentik_client.models.geoip_binding_enum import GeoipBindingEnum
from authentik_client.models.network_binding_enum import NetworkBindingEnum
from typing import Optional, Set
from typing_extensions import Self

class UserLoginStageRequest(BaseModel):
    """
    UserLoginStage Serializer
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)]
    flow_set: Optional[List[FlowSetRequest]] = None
    session_duration: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Determines how long a session lasts. Default of 0 means that the sessions lasts until the browser is closed. (Format: hours=-1;minutes=-2;seconds=-3)")
    terminate_other_sessions: Optional[StrictBool] = Field(default=None, description="Terminate all other sessions of the user logging in.")
    remember_me_offset: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Offset the session will be extended by when the user picks the remember me option. Default of 0 means that the remember me option will not be shown. (Format: hours=-1;minutes=-2;seconds=-3)")
    network_binding: Optional[NetworkBindingEnum] = Field(default=None, description="Bind sessions created by this stage to the configured network")
    geoip_binding: Optional[GeoipBindingEnum] = Field(default=None, description="Bind sessions created by this stage to the configured GeoIP location")
    __properties: ClassVar[List[str]] = ["name", "flow_set", "session_duration", "terminate_other_sessions", "remember_me_offset", "network_binding", "geoip_binding"]

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
        """Create an instance of UserLoginStageRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item in self.flow_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flow_set'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserLoginStageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "flow_set": [FlowSetRequest.from_dict(_item) for _item in obj["flow_set"]] if obj.get("flow_set") is not None else None,
            "session_duration": obj.get("session_duration"),
            "terminate_other_sessions": obj.get("terminate_other_sessions"),
            "remember_me_offset": obj.get("remember_me_offset"),
            "network_binding": obj.get("network_binding"),
            "geoip_binding": obj.get("geoip_binding")
        })
        return _obj


