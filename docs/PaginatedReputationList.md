# PaginatedReputationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Reputation]**](Reputation.md) |  | 

## Example

```python
from authentik_client.models.paginated_reputation_list import PaginatedReputationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedReputationList from a JSON string
paginated_reputation_list_instance = PaginatedReputationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedReputationList.to_json())

# convert the object into a dict
paginated_reputation_list_dict = paginated_reputation_list_instance.to_dict()
# create an instance of PaginatedReputationList from a dict
paginated_reputation_list_form_dict = paginated_reputation_list.from_dict(paginated_reputation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


