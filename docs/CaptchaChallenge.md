# CaptchaChallenge

Site public key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-captcha']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**site_key** | **str** |  | 
**js_url** | **str** |  | 
**interactive** | **bool** |  | 

## Example

```python
from authentik_client.models.captcha_challenge import CaptchaChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of CaptchaChallenge from a JSON string
captcha_challenge_instance = CaptchaChallenge.from_json(json)
# print the JSON string representation of the object
print(CaptchaChallenge.to_json())

# convert the object into a dict
captcha_challenge_dict = captcha_challenge_instance.to_dict()
# create an instance of CaptchaChallenge from a dict
captcha_challenge_form_dict = captcha_challenge.from_dict(captcha_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


