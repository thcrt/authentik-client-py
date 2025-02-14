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
from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from authentik_client.models.license_flags_enum import LicenseFlagsEnum
from authentik_client.models.license_summary_status_enum import LicenseSummaryStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class LicenseSummary(BaseModel):
    """
    Serializer for license status
    """ # noqa: E501
    internal_users: StrictInt
    external_users: StrictInt
    status: LicenseSummaryStatusEnum
    latest_valid: datetime
    license_flags: List[LicenseFlagsEnum]
    __properties: ClassVar[List[str]] = ["internal_users", "external_users", "status", "latest_valid", "license_flags"]

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
        """Create an instance of LicenseSummary from a JSON string"""
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
        """Create an instance of LicenseSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "internal_users": obj.get("internal_users"),
            "external_users": obj.get("external_users"),
            "status": obj.get("status"),
            "latest_valid": obj.get("latest_valid"),
            "license_flags": obj.get("license_flags")
        })
        return _obj


