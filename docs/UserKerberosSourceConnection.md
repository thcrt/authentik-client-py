# UserKerberosSourceConnection

Kerberos Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**user** | **int** |  | 
**source** | [**Source**](Source.md) |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.user_kerberos_source_connection import UserKerberosSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of UserKerberosSourceConnection from a JSON string
user_kerberos_source_connection_instance = UserKerberosSourceConnection.from_json(json)
# print the JSON string representation of the object
print(UserKerberosSourceConnection.to_json())

# convert the object into a dict
user_kerberos_source_connection_dict = user_kerberos_source_connection_instance.to_dict()
# create an instance of UserKerberosSourceConnection from a dict
user_kerberos_source_connection_form_dict = user_kerberos_source_connection.from_dict(user_kerberos_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


