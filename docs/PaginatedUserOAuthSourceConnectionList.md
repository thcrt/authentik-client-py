# PaginatedUserOAuthSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserOAuthSourceConnection]**](UserOAuthSourceConnection.md) |  | 

## Example

```python
from authentik_client.models.paginated_user_o_auth_source_connection_list import PaginatedUserOAuthSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserOAuthSourceConnectionList from a JSON string
paginated_user_o_auth_source_connection_list_instance = PaginatedUserOAuthSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserOAuthSourceConnectionList.to_json())

# convert the object into a dict
paginated_user_o_auth_source_connection_list_dict = paginated_user_o_auth_source_connection_list_instance.to_dict()
# create an instance of PaginatedUserOAuthSourceConnectionList from a dict
paginated_user_o_auth_source_connection_list_form_dict = paginated_user_o_auth_source_connection_list.from_dict(paginated_user_o_auth_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


