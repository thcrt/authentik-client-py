# PatchedAuthenticatorValidateStageRequest

AuthenticatorValidateStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**not_configured_action** | [**NotConfiguredActionEnum**](NotConfiguredActionEnum.md) |  | [optional] 
**device_classes** | [**List[DeviceClassesEnum]**](DeviceClassesEnum.md) | Device classes which can be used to authenticate | [optional] 
**configuration_stages** | **List[str]** | Stages used to configure Authenticator when user doesn&#39;t have any compatible devices. After this configuration Stage passes, the user is not prompted again. | [optional] 
**last_auth_threshold** | **str** | If any of the user&#39;s device has been used within this threshold, this stage will be skipped | [optional] 
**webauthn_user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) | Enforce user verification for WebAuthn devices. | [optional] 
**webauthn_allowed_device_types** | **List[str]** |  | [optional] 

## Example

```python
from authentik_client.models.patched_authenticator_validate_stage_request import PatchedAuthenticatorValidateStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAuthenticatorValidateStageRequest from a JSON string
patched_authenticator_validate_stage_request_instance = PatchedAuthenticatorValidateStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAuthenticatorValidateStageRequest.to_json())

# convert the object into a dict
patched_authenticator_validate_stage_request_dict = patched_authenticator_validate_stage_request_instance.to_dict()
# create an instance of PatchedAuthenticatorValidateStageRequest from a dict
patched_authenticator_validate_stage_request_form_dict = patched_authenticator_validate_stage_request.from_dict(patched_authenticator_validate_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


