# PaginatedStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Stage]**](Stage.md) |  | 

## Example

```python
from authentik_client.models.paginated_stage_list import PaginatedStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedStageList from a JSON string
paginated_stage_list_instance = PaginatedStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedStageList.to_json())

# convert the object into a dict
paginated_stage_list_dict = paginated_stage_list_instance.to_dict()
# create an instance of PaginatedStageList from a dict
paginated_stage_list_form_dict = paginated_stage_list.from_dict(paginated_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


