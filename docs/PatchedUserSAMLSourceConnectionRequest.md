# PatchedUserSAMLSourceConnectionRequest

SAML Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_user_saml_source_connection_request import PatchedUserSAMLSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserSAMLSourceConnectionRequest from a JSON string
patched_user_saml_source_connection_request_instance = PatchedUserSAMLSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserSAMLSourceConnectionRequest.to_json())

# convert the object into a dict
patched_user_saml_source_connection_request_dict = patched_user_saml_source_connection_request_instance.to_dict()
# create an instance of PatchedUserSAMLSourceConnectionRequest from a dict
patched_user_saml_source_connection_request_form_dict = patched_user_saml_source_connection_request.from_dict(patched_user_saml_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


