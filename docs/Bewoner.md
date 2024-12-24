# Bewoner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burgerservicenummer** | **str** |  | [optional] 
**geheimhouding_persoonsgegevens** | **bool** | Indicatie dat persoonsgegevens niet mogen worden verstrekt aan derden / maatschappelijke instellingen.  | [optional] 
**in_onderzoek** | **bool** | Geeft aan dat de verblijfplaats in onderzoek is.  | [optional] 
**naam** | [**Naam**](Naam.md) |  | [optional] 
**geboorte** | [**GeboorteBasis**](GeboorteBasis.md) |  | [optional] 

## Example

```python
from brp_bewoning_client.models.bewoner import Bewoner

# TODO update the JSON string below
json = "{}"
# create an instance of Bewoner from a JSON string
bewoner_instance = Bewoner.from_json(json)
# print the JSON string representation of the object
print(Bewoner.to_json())

# convert the object into a dict
bewoner_dict = bewoner_instance.to_dict()
# create an instance of Bewoner from a dict
bewoner_from_dict = Bewoner.from_dict(bewoner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


