# TransactionApplicationRequest

Serializer for creating a provider and an application in one transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**ApplicationRequest**](ApplicationRequest.md) |  | 
**provider_model** | [**ProviderModelEnum**](ProviderModelEnum.md) |  | 
**provider** | [**ModelRequest**](ModelRequest.md) |  | 
**policy_bindings** | [**List[TransactionPolicyBindingRequest]**](TransactionPolicyBindingRequest.md) |  | [optional] 

## Example

```python
from authentik_client.models.transaction_application_request import TransactionApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionApplicationRequest from a JSON string
transaction_application_request_instance = TransactionApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionApplicationRequest.to_json())

# convert the object into a dict
transaction_application_request_dict = transaction_application_request_instance.to_dict()
# create an instance of TransactionApplicationRequest from a dict
transaction_application_request_form_dict = transaction_application_request.from_dict(transaction_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


