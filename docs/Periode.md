# Periode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_van** | **date** | De begindatum van de periode.  | [optional] 
**datum_tot** | **date** | De einddatum van de periode.  | [optional] 

## Example

```python
from brp_bewoning_client.models.periode import Periode

# TODO update the JSON string below
json = "{}"
# create an instance of Periode from a JSON string
periode_instance = Periode.from_json(json)
# print the JSON string representation of the object
print(Periode.to_json())

# convert the object into a dict
periode_dict = periode_instance.to_dict()
# create an instance of Periode from a dict
periode_from_dict = Periode.from_dict(periode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


