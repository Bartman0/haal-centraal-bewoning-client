# BadRequestFoutbericht


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Link naar meer informatie over deze fout | [optional] 
**title** | **str** | Beschrijving van de fout | [optional] 
**status** | **int** | Http status code | [optional] 
**detail** | **str** | Details over de fout | [optional] 
**instance** | **str** | Uri van de aanroep die de fout heeft veroorzaakt | [optional] 
**code** | **str** | Systeemcode die het type fout aangeeft | [optional] 
**invalid_params** | [**List[InvalidParam]**](InvalidParam.md) | Foutmelding per fout in een parameter. Alle gevonden fouten worden één keer teruggemeld.  | [optional] 

## Example

```python
from brp_bewoning_client.models.bad_request_foutbericht import BadRequestFoutbericht

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestFoutbericht from a JSON string
bad_request_foutbericht_instance = BadRequestFoutbericht.from_json(json)
# print the JSON string representation of the object
print(BadRequestFoutbericht.to_json())

# convert the object into a dict
bad_request_foutbericht_dict = bad_request_foutbericht_instance.to_dict()
# create an instance of BadRequestFoutbericht from a dict
bad_request_foutbericht_from_dict = BadRequestFoutbericht.from_dict(bad_request_foutbericht_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


