# ShellChallenge

challenge type to render HTML as-is

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'xak-flow-shell']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**body** | **str** |  | 

## Example

```python
from authentik_client.models.shell_challenge import ShellChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of ShellChallenge from a JSON string
shell_challenge_instance = ShellChallenge.from_json(json)
# print the JSON string representation of the object
print(ShellChallenge.to_json())

# convert the object into a dict
shell_challenge_dict = shell_challenge_instance.to_dict()
# create an instance of ShellChallenge from a dict
shell_challenge_form_dict = shell_challenge.from_dict(shell_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


