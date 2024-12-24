# VolledigeDatum

Datum conform iso8601

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum** | **date** |  | 

## Example

```python
from brp_bewoning_client.models.volledige_datum import VolledigeDatum

# TODO update the JSON string below
json = "{}"
# create an instance of VolledigeDatum from a JSON string
volledige_datum_instance = VolledigeDatum.from_json(json)
# print the JSON string representation of the object
print(VolledigeDatum.to_json())

# convert the object into a dict
volledige_datum_dict = volledige_datum_instance.to_dict()
# create an instance of VolledigeDatum from a dict
volledige_datum_from_dict = VolledigeDatum.from_dict(volledige_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


