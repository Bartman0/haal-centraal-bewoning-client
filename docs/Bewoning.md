# Bewoning

Een bewoning geeft aan welke personen in een periode (mogelijk) op een adresseerbaar object staan ingeschreven.  Een persoon is een mogelijke bewoner als niet met zekerheid kan worden bepaald of de persoon in de bewoningperiode op het adresseerbaar object staat/stond ingeschreven. Dit is het geval als de datum aanvang of de datum einde van de inschrijving geheel of deels onbekend is, en de onzekerheidsperiode overlapt de bewoningperiode.  Wanneer een bewoning in totaal meer dan 100 bewoners en/of mogelijke bewoners heeft, wordt het **indicatieVeelBewoners** veld geleverd. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adresseerbaar_object_identificatie** | **str** | De identificatiecode van een adresseerbaar object.  | [optional] 
**periode** | [**Periode**](Periode.md) |  | [optional] 
**bewoners** | [**List[Bewoner]**](Bewoner.md) | De personen die in de bewoning periode staan ingeschreven op het adresseerbaar object.  | [optional] 
**mogelijke_bewoners** | [**List[Bewoner]**](Bewoner.md) | De personen die in de bewoning periode mogelijk staan ingeschreven op het adresseerbaar object.  | [optional] 
**indicatie_veel_bewoners** | **bool** | Geeft aan dat de bewoning in totaal meer dan 100 bewoners en/of mogelijke bewoners heeft.  | [optional] 

## Example

```python
from brp_bewoning_client.models.bewoning import Bewoning

# TODO update the JSON string below
json = "{}"
# create an instance of Bewoning from a JSON string
bewoning_instance = Bewoning.from_json(json)
# print the JSON string representation of the object
print(Bewoning.to_json())

# convert the object into a dict
bewoning_dict = bewoning_instance.to_dict()
# create an instance of Bewoning from a dict
bewoning_from_dict = Bewoning.from_dict(bewoning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


