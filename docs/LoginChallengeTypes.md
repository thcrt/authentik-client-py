# LoginChallengeTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-source-plex']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**to** | **str** |  | 
**client_id** | **str** |  | 
**scope** | **str** |  | 
**redirect_uri** | **str** |  | 
**state** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from authentik_client.models.login_challenge_types import LoginChallengeTypes

# TODO update the JSON string below
json = "{}"
# create an instance of LoginChallengeTypes from a JSON string
login_challenge_types_instance = LoginChallengeTypes.from_json(json)
# print the JSON string representation of the object
print(LoginChallengeTypes.to_json())

# convert the object into a dict
login_challenge_types_dict = login_challenge_types_instance.to_dict()
# create an instance of LoginChallengeTypes from a dict
login_challenge_types_form_dict = login_challenge_types.from_dict(login_challenge_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


