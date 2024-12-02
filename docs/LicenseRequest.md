# LicenseRequest

License Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 

## Example

```python
from authentik_client.models.license_request import LicenseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseRequest from a JSON string
license_request_instance = LicenseRequest.from_json(json)
# print the JSON string representation of the object
print(LicenseRequest.to_json())

# convert the object into a dict
license_request_dict = license_request_instance.to_dict()
# create an instance of LicenseRequest from a dict
license_request_form_dict = license_request.from_dict(license_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


