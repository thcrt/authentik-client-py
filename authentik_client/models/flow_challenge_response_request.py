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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from authentik_client.models.apple_challenge_response_request import AppleChallengeResponseRequest
from authentik_client.models.authenticator_duo_challenge_response_request import AuthenticatorDuoChallengeResponseRequest
from authentik_client.models.authenticator_sms_challenge_response_request import AuthenticatorSMSChallengeResponseRequest
from authentik_client.models.authenticator_static_challenge_response_request import AuthenticatorStaticChallengeResponseRequest
from authentik_client.models.authenticator_totp_challenge_response_request import AuthenticatorTOTPChallengeResponseRequest
from authentik_client.models.authenticator_validation_challenge_response_request import AuthenticatorValidationChallengeResponseRequest
from authentik_client.models.authenticator_web_authn_challenge_response_request import AuthenticatorWebAuthnChallengeResponseRequest
from authentik_client.models.auto_submit_challenge_response_request import AutoSubmitChallengeResponseRequest
from authentik_client.models.captcha_challenge_response_request import CaptchaChallengeResponseRequest
from authentik_client.models.consent_challenge_response_request import ConsentChallengeResponseRequest
from authentik_client.models.dummy_challenge_response_request import DummyChallengeResponseRequest
from authentik_client.models.email_challenge_response_request import EmailChallengeResponseRequest
from authentik_client.models.frame_challenge_response_request import FrameChallengeResponseRequest
from authentik_client.models.identification_challenge_response_request import IdentificationChallengeResponseRequest
from authentik_client.models.o_auth_device_code_challenge_response_request import OAuthDeviceCodeChallengeResponseRequest
from authentik_client.models.o_auth_device_code_finish_challenge_response_request import OAuthDeviceCodeFinishChallengeResponseRequest
from authentik_client.models.password_challenge_response_request import PasswordChallengeResponseRequest
from authentik_client.models.plex_authentication_challenge_response_request import PlexAuthenticationChallengeResponseRequest
from authentik_client.models.prompt_challenge_response_request import PromptChallengeResponseRequest
from authentik_client.models.user_login_challenge_response_request import UserLoginChallengeResponseRequest
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

FLOWCHALLENGERESPONSEREQUEST_ONE_OF_SCHEMAS = ["AppleChallengeResponseRequest", "AuthenticatorDuoChallengeResponseRequest", "AuthenticatorSMSChallengeResponseRequest", "AuthenticatorStaticChallengeResponseRequest", "AuthenticatorTOTPChallengeResponseRequest", "AuthenticatorValidationChallengeResponseRequest", "AuthenticatorWebAuthnChallengeResponseRequest", "AutoSubmitChallengeResponseRequest", "CaptchaChallengeResponseRequest", "ConsentChallengeResponseRequest", "DummyChallengeResponseRequest", "EmailChallengeResponseRequest", "FrameChallengeResponseRequest", "IdentificationChallengeResponseRequest", "OAuthDeviceCodeChallengeResponseRequest", "OAuthDeviceCodeFinishChallengeResponseRequest", "PasswordChallengeResponseRequest", "PlexAuthenticationChallengeResponseRequest", "PromptChallengeResponseRequest", "UserLoginChallengeResponseRequest"]

class FlowChallengeResponseRequest(BaseModel):
    """
    FlowChallengeResponseRequest
    """
    # data type: AppleChallengeResponseRequest
    oneof_schema_1_validator: Optional[AppleChallengeResponseRequest] = None
    # data type: AuthenticatorDuoChallengeResponseRequest
    oneof_schema_2_validator: Optional[AuthenticatorDuoChallengeResponseRequest] = None
    # data type: AuthenticatorSMSChallengeResponseRequest
    oneof_schema_3_validator: Optional[AuthenticatorSMSChallengeResponseRequest] = None
    # data type: AuthenticatorStaticChallengeResponseRequest
    oneof_schema_4_validator: Optional[AuthenticatorStaticChallengeResponseRequest] = None
    # data type: AuthenticatorTOTPChallengeResponseRequest
    oneof_schema_5_validator: Optional[AuthenticatorTOTPChallengeResponseRequest] = None
    # data type: AuthenticatorValidationChallengeResponseRequest
    oneof_schema_6_validator: Optional[AuthenticatorValidationChallengeResponseRequest] = None
    # data type: AuthenticatorWebAuthnChallengeResponseRequest
    oneof_schema_7_validator: Optional[AuthenticatorWebAuthnChallengeResponseRequest] = None
    # data type: AutoSubmitChallengeResponseRequest
    oneof_schema_8_validator: Optional[AutoSubmitChallengeResponseRequest] = None
    # data type: CaptchaChallengeResponseRequest
    oneof_schema_9_validator: Optional[CaptchaChallengeResponseRequest] = None
    # data type: ConsentChallengeResponseRequest
    oneof_schema_10_validator: Optional[ConsentChallengeResponseRequest] = None
    # data type: DummyChallengeResponseRequest
    oneof_schema_11_validator: Optional[DummyChallengeResponseRequest] = None
    # data type: EmailChallengeResponseRequest
    oneof_schema_12_validator: Optional[EmailChallengeResponseRequest] = None
    # data type: FrameChallengeResponseRequest
    oneof_schema_13_validator: Optional[FrameChallengeResponseRequest] = None
    # data type: IdentificationChallengeResponseRequest
    oneof_schema_14_validator: Optional[IdentificationChallengeResponseRequest] = None
    # data type: OAuthDeviceCodeChallengeResponseRequest
    oneof_schema_15_validator: Optional[OAuthDeviceCodeChallengeResponseRequest] = None
    # data type: OAuthDeviceCodeFinishChallengeResponseRequest
    oneof_schema_16_validator: Optional[OAuthDeviceCodeFinishChallengeResponseRequest] = None
    # data type: PasswordChallengeResponseRequest
    oneof_schema_17_validator: Optional[PasswordChallengeResponseRequest] = None
    # data type: PlexAuthenticationChallengeResponseRequest
    oneof_schema_18_validator: Optional[PlexAuthenticationChallengeResponseRequest] = None
    # data type: PromptChallengeResponseRequest
    oneof_schema_19_validator: Optional[PromptChallengeResponseRequest] = None
    # data type: UserLoginChallengeResponseRequest
    oneof_schema_20_validator: Optional[UserLoginChallengeResponseRequest] = None
    actual_instance: Optional[Union[AppleChallengeResponseRequest, AuthenticatorDuoChallengeResponseRequest, AuthenticatorSMSChallengeResponseRequest, AuthenticatorStaticChallengeResponseRequest, AuthenticatorTOTPChallengeResponseRequest, AuthenticatorValidationChallengeResponseRequest, AuthenticatorWebAuthnChallengeResponseRequest, AutoSubmitChallengeResponseRequest, CaptchaChallengeResponseRequest, ConsentChallengeResponseRequest, DummyChallengeResponseRequest, EmailChallengeResponseRequest, FrameChallengeResponseRequest, IdentificationChallengeResponseRequest, OAuthDeviceCodeChallengeResponseRequest, OAuthDeviceCodeFinishChallengeResponseRequest, PasswordChallengeResponseRequest, PlexAuthenticationChallengeResponseRequest, PromptChallengeResponseRequest, UserLoginChallengeResponseRequest]] = None
    one_of_schemas: List[str] = Field(default=Literal["AppleChallengeResponseRequest", "AuthenticatorDuoChallengeResponseRequest", "AuthenticatorSMSChallengeResponseRequest", "AuthenticatorStaticChallengeResponseRequest", "AuthenticatorTOTPChallengeResponseRequest", "AuthenticatorValidationChallengeResponseRequest", "AuthenticatorWebAuthnChallengeResponseRequest", "AutoSubmitChallengeResponseRequest", "CaptchaChallengeResponseRequest", "ConsentChallengeResponseRequest", "DummyChallengeResponseRequest", "EmailChallengeResponseRequest", "FrameChallengeResponseRequest", "IdentificationChallengeResponseRequest", "OAuthDeviceCodeChallengeResponseRequest", "OAuthDeviceCodeFinishChallengeResponseRequest", "PasswordChallengeResponseRequest", "PlexAuthenticationChallengeResponseRequest", "PromptChallengeResponseRequest", "UserLoginChallengeResponseRequest"])

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = FlowChallengeResponseRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: AppleChallengeResponseRequest
        if not isinstance(v, AppleChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AppleChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: AuthenticatorDuoChallengeResponseRequest
        if not isinstance(v, AuthenticatorDuoChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorDuoChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: AuthenticatorSMSChallengeResponseRequest
        if not isinstance(v, AuthenticatorSMSChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorSMSChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: AuthenticatorStaticChallengeResponseRequest
        if not isinstance(v, AuthenticatorStaticChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorStaticChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: AuthenticatorTOTPChallengeResponseRequest
        if not isinstance(v, AuthenticatorTOTPChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorTOTPChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: AuthenticatorValidationChallengeResponseRequest
        if not isinstance(v, AuthenticatorValidationChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorValidationChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: AuthenticatorWebAuthnChallengeResponseRequest
        if not isinstance(v, AuthenticatorWebAuthnChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorWebAuthnChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: AutoSubmitChallengeResponseRequest
        if not isinstance(v, AutoSubmitChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AutoSubmitChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: CaptchaChallengeResponseRequest
        if not isinstance(v, CaptchaChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CaptchaChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: ConsentChallengeResponseRequest
        if not isinstance(v, ConsentChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConsentChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: DummyChallengeResponseRequest
        if not isinstance(v, DummyChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DummyChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: EmailChallengeResponseRequest
        if not isinstance(v, EmailChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EmailChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: FrameChallengeResponseRequest
        if not isinstance(v, FrameChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FrameChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: IdentificationChallengeResponseRequest
        if not isinstance(v, IdentificationChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: OAuthDeviceCodeChallengeResponseRequest
        if not isinstance(v, OAuthDeviceCodeChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OAuthDeviceCodeChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: OAuthDeviceCodeFinishChallengeResponseRequest
        if not isinstance(v, OAuthDeviceCodeFinishChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OAuthDeviceCodeFinishChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: PasswordChallengeResponseRequest
        if not isinstance(v, PasswordChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PasswordChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: PlexAuthenticationChallengeResponseRequest
        if not isinstance(v, PlexAuthenticationChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlexAuthenticationChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: PromptChallengeResponseRequest
        if not isinstance(v, PromptChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PromptChallengeResponseRequest`")
        else:
            match += 1
        # validate data type: UserLoginChallengeResponseRequest
        if not isinstance(v, UserLoginChallengeResponseRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserLoginChallengeResponseRequest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FlowChallengeResponseRequest with oneOf schemas: AppleChallengeResponseRequest, AuthenticatorDuoChallengeResponseRequest, AuthenticatorSMSChallengeResponseRequest, AuthenticatorStaticChallengeResponseRequest, AuthenticatorTOTPChallengeResponseRequest, AuthenticatorValidationChallengeResponseRequest, AuthenticatorWebAuthnChallengeResponseRequest, AutoSubmitChallengeResponseRequest, CaptchaChallengeResponseRequest, ConsentChallengeResponseRequest, DummyChallengeResponseRequest, EmailChallengeResponseRequest, FrameChallengeResponseRequest, IdentificationChallengeResponseRequest, OAuthDeviceCodeChallengeResponseRequest, OAuthDeviceCodeFinishChallengeResponseRequest, PasswordChallengeResponseRequest, PlexAuthenticationChallengeResponseRequest, PromptChallengeResponseRequest, UserLoginChallengeResponseRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FlowChallengeResponseRequest with oneOf schemas: AppleChallengeResponseRequest, AuthenticatorDuoChallengeResponseRequest, AuthenticatorSMSChallengeResponseRequest, AuthenticatorStaticChallengeResponseRequest, AuthenticatorTOTPChallengeResponseRequest, AuthenticatorValidationChallengeResponseRequest, AuthenticatorWebAuthnChallengeResponseRequest, AutoSubmitChallengeResponseRequest, CaptchaChallengeResponseRequest, ConsentChallengeResponseRequest, DummyChallengeResponseRequest, EmailChallengeResponseRequest, FrameChallengeResponseRequest, IdentificationChallengeResponseRequest, OAuthDeviceCodeChallengeResponseRequest, OAuthDeviceCodeFinishChallengeResponseRequest, PasswordChallengeResponseRequest, PlexAuthenticationChallengeResponseRequest, PromptChallengeResponseRequest, UserLoginChallengeResponseRequest. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AppleChallengeResponseRequest
        try:
            instance.actual_instance = AppleChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorDuoChallengeResponseRequest
        try:
            instance.actual_instance = AuthenticatorDuoChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorSMSChallengeResponseRequest
        try:
            instance.actual_instance = AuthenticatorSMSChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorStaticChallengeResponseRequest
        try:
            instance.actual_instance = AuthenticatorStaticChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorTOTPChallengeResponseRequest
        try:
            instance.actual_instance = AuthenticatorTOTPChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorValidationChallengeResponseRequest
        try:
            instance.actual_instance = AuthenticatorValidationChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorWebAuthnChallengeResponseRequest
        try:
            instance.actual_instance = AuthenticatorWebAuthnChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AutoSubmitChallengeResponseRequest
        try:
            instance.actual_instance = AutoSubmitChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CaptchaChallengeResponseRequest
        try:
            instance.actual_instance = CaptchaChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConsentChallengeResponseRequest
        try:
            instance.actual_instance = ConsentChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DummyChallengeResponseRequest
        try:
            instance.actual_instance = DummyChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EmailChallengeResponseRequest
        try:
            instance.actual_instance = EmailChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FrameChallengeResponseRequest
        try:
            instance.actual_instance = FrameChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationChallengeResponseRequest
        try:
            instance.actual_instance = IdentificationChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OAuthDeviceCodeChallengeResponseRequest
        try:
            instance.actual_instance = OAuthDeviceCodeChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OAuthDeviceCodeFinishChallengeResponseRequest
        try:
            instance.actual_instance = OAuthDeviceCodeFinishChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PasswordChallengeResponseRequest
        try:
            instance.actual_instance = PasswordChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PlexAuthenticationChallengeResponseRequest
        try:
            instance.actual_instance = PlexAuthenticationChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PromptChallengeResponseRequest
        try:
            instance.actual_instance = PromptChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserLoginChallengeResponseRequest
        try:
            instance.actual_instance = UserLoginChallengeResponseRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FlowChallengeResponseRequest with oneOf schemas: AppleChallengeResponseRequest, AuthenticatorDuoChallengeResponseRequest, AuthenticatorSMSChallengeResponseRequest, AuthenticatorStaticChallengeResponseRequest, AuthenticatorTOTPChallengeResponseRequest, AuthenticatorValidationChallengeResponseRequest, AuthenticatorWebAuthnChallengeResponseRequest, AutoSubmitChallengeResponseRequest, CaptchaChallengeResponseRequest, ConsentChallengeResponseRequest, DummyChallengeResponseRequest, EmailChallengeResponseRequest, FrameChallengeResponseRequest, IdentificationChallengeResponseRequest, OAuthDeviceCodeChallengeResponseRequest, OAuthDeviceCodeFinishChallengeResponseRequest, PasswordChallengeResponseRequest, PlexAuthenticationChallengeResponseRequest, PromptChallengeResponseRequest, UserLoginChallengeResponseRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FlowChallengeResponseRequest with oneOf schemas: AppleChallengeResponseRequest, AuthenticatorDuoChallengeResponseRequest, AuthenticatorSMSChallengeResponseRequest, AuthenticatorStaticChallengeResponseRequest, AuthenticatorTOTPChallengeResponseRequest, AuthenticatorValidationChallengeResponseRequest, AuthenticatorWebAuthnChallengeResponseRequest, AutoSubmitChallengeResponseRequest, CaptchaChallengeResponseRequest, ConsentChallengeResponseRequest, DummyChallengeResponseRequest, EmailChallengeResponseRequest, FrameChallengeResponseRequest, IdentificationChallengeResponseRequest, OAuthDeviceCodeChallengeResponseRequest, OAuthDeviceCodeFinishChallengeResponseRequest, PasswordChallengeResponseRequest, PlexAuthenticationChallengeResponseRequest, PromptChallengeResponseRequest, UserLoginChallengeResponseRequest. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AppleChallengeResponseRequest, AuthenticatorDuoChallengeResponseRequest, AuthenticatorSMSChallengeResponseRequest, AuthenticatorStaticChallengeResponseRequest, AuthenticatorTOTPChallengeResponseRequest, AuthenticatorValidationChallengeResponseRequest, AuthenticatorWebAuthnChallengeResponseRequest, AutoSubmitChallengeResponseRequest, CaptchaChallengeResponseRequest, ConsentChallengeResponseRequest, DummyChallengeResponseRequest, EmailChallengeResponseRequest, FrameChallengeResponseRequest, IdentificationChallengeResponseRequest, OAuthDeviceCodeChallengeResponseRequest, OAuthDeviceCodeFinishChallengeResponseRequest, PasswordChallengeResponseRequest, PlexAuthenticationChallengeResponseRequest, PromptChallengeResponseRequest, UserLoginChallengeResponseRequest]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


