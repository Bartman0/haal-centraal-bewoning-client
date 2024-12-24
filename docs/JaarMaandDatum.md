# JaarMaandDatum

representatie voor een datum waarvan de dag onbekend is

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jaar** | **int** |  | 
**maand** | **int** |  | 

## Example

```python
from brp_bewoning_client.models.jaar_maand_datum import JaarMaandDatum

# TODO update the JSON string below
json = "{}"
# create an instance of JaarMaandDatum from a JSON string
jaar_maand_datum_instance = JaarMaandDatum.from_json(json)
# print the JSON string representation of the object
print(JaarMaandDatum.to_json())

# convert the object into a dict
jaar_maand_datum_dict = jaar_maand_datum_instance.to_dict()
# create an instance of JaarMaandDatum from a dict
jaar_maand_datum_from_dict = JaarMaandDatum.from_dict(jaar_maand_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


