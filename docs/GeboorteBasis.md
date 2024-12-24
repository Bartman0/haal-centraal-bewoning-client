# GeboorteBasis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 

## Example

```python
from brp_bewoning_client.models.geboorte_basis import GeboorteBasis

# TODO update the JSON string below
json = "{}"
# create an instance of GeboorteBasis from a JSON string
geboorte_basis_instance = GeboorteBasis.from_json(json)
# print the JSON string representation of the object
print(GeboorteBasis.to_json())

# convert the object into a dict
geboorte_basis_dict = geboorte_basis_instance.to_dict()
# create an instance of GeboorteBasis from a dict
geboorte_basis_from_dict = GeboorteBasis.from_dict(geboorte_basis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


