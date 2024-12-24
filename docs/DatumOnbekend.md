# DatumOnbekend

representatie voor een volledig onbekend datum

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onbekend** | **bool** |  | [default to True]

## Example

```python
from brp_bewoning_client.models.datum_onbekend import DatumOnbekend

# TODO update the JSON string below
json = "{}"
# create an instance of DatumOnbekend from a JSON string
datum_onbekend_instance = DatumOnbekend.from_json(json)
# print the JSON string representation of the object
print(DatumOnbekend.to_json())

# convert the object into a dict
datum_onbekend_dict = datum_onbekend_instance.to_dict()
# create an instance of DatumOnbekend from a dict
datum_onbekend_from_dict = DatumOnbekend.from_dict(datum_onbekend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


