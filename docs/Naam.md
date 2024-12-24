# Naam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volledige_naam** | **str** | Combinatie van predicaat, voornamen, adellijke titel, voorvoegsels en geslachtsnaam, zonder toevoeging van een eventuele partnernaam.  | [optional] 

## Example

```python
from brp_bewoning_client.models.naam import Naam

# TODO update the JSON string below
json = "{}"
# create an instance of Naam from a JSON string
naam_instance = Naam.from_json(json)
# print the JSON string representation of the object
print(Naam.to_json())

# convert the object into a dict
naam_dict = naam_instance.to_dict()
# create an instance of Naam from a dict
naam_from_dict = Naam.from_dict(naam_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


