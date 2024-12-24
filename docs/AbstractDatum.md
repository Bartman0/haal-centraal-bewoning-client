# AbstractDatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**lang_formaat** | **str** |  | 

## Example

```python
from brp_bewoning_client.models.abstract_datum import AbstractDatum

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractDatum from a JSON string
abstract_datum_instance = AbstractDatum.from_json(json)
# print the JSON string representation of the object
print(AbstractDatum.to_json())

# convert the object into a dict
abstract_datum_dict = abstract_datum_instance.to_dict()
# create an instance of AbstractDatum from a dict
abstract_datum_from_dict = AbstractDatum.from_dict(abstract_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


