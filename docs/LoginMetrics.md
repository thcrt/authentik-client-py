# LoginMetrics

Login Metrics per 1h

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logins** | [**List[Coordinate]**](Coordinate.md) |  | [readonly] 
**logins_failed** | [**List[Coordinate]**](Coordinate.md) |  | [readonly] 
**authorizations** | [**List[Coordinate]**](Coordinate.md) |  | [readonly] 

## Example

```python
from authentik_client.models.login_metrics import LoginMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of LoginMetrics from a JSON string
login_metrics_instance = LoginMetrics.from_json(json)
# print the JSON string representation of the object
print(LoginMetrics.to_json())

# convert the object into a dict
login_metrics_dict = login_metrics_instance.to_dict()
# create an instance of LoginMetrics from a dict
login_metrics_form_dict = login_metrics.from_dict(login_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


