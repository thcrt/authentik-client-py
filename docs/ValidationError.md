# ValidationError

Validation Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_field_errors** | **List[str]** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.validation_error import ValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError from a JSON string
validation_error_instance = ValidationError.from_json(json)
# print the JSON string representation of the object
print(ValidationError.to_json())

# convert the object into a dict
validation_error_dict = validation_error_instance.to_dict()
# create an instance of ValidationError from a dict
validation_error_form_dict = validation_error.from_dict(validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


