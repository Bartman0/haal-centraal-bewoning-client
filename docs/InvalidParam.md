# InvalidParam

Details over fouten in opgegeven parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** | Naam van de parameter | [optional] 
**code** | **str** | Systeemcode die het type fout aangeeft | [optional] 
**reason** | **str** | Beschrijving van de fout op de parameterwaarde | [optional] 

## Example

```python
from brp_bewoning_client.models.invalid_param import InvalidParam

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParam from a JSON string
invalid_param_instance = InvalidParam.from_json(json)
# print the JSON string representation of the object
print(InvalidParam.to_json())

# convert the object into a dict
invalid_param_dict = invalid_param_instance.to_dict()
# create an instance of InvalidParam from a dict
invalid_param_from_dict = InvalidParam.from_dict(invalid_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


