# Foutbericht

Terugmelding bij een fout. JSON representatie in lijn met [RFC7807](https://tools.ietf.org/html/rfc7807).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Link naar meer informatie over deze fout | [optional] 
**title** | **str** | Beschrijving van de fout | [optional] 
**status** | **int** | Http status code | [optional] 
**detail** | **str** | Details over de fout | [optional] 
**instance** | **str** | Uri van de aanroep die de fout heeft veroorzaakt | [optional] 
**code** | **str** | Systeemcode die het type fout aangeeft | [optional] 

## Example

```python
from brp_bewoning_client.models.foutbericht import Foutbericht

# TODO update the JSON string below
json = "{}"
# create an instance of Foutbericht from a JSON string
foutbericht_instance = Foutbericht.from_json(json)
# print the JSON string representation of the object
print(Foutbericht.to_json())

# convert the object into a dict
foutbericht_dict = foutbericht_instance.to_dict()
# create an instance of Foutbericht from a dict
foutbericht_from_dict = Foutbericht.from_dict(foutbericht_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


