# JaarDatum

representatie voor een datum waarvan maand en dag onbekend zijn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jaar** | **int** |  | 

## Example

```python
from brp_bewoning_client.models.jaar_datum import JaarDatum

# TODO update the JSON string below
json = "{}"
# create an instance of JaarDatum from a JSON string
jaar_datum_instance = JaarDatum.from_json(json)
# print the JSON string representation of the object
print(JaarDatum.to_json())

# convert the object into a dict
jaar_datum_dict = jaar_datum_instance.to_dict()
# create an instance of JaarDatum from a dict
jaar_datum_from_dict = JaarDatum.from_dict(jaar_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


