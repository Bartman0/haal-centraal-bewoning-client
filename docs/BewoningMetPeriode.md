# BewoningMetPeriode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_van** | **date** |  | 
**datum_tot** | **date** |  | 
**adresseerbaar_object_identificatie** | **str** | De identificatiecode van een adresseerbaar object uitgezonderd de standaardwaarde (0000000000000000)  | 

## Example

```python
from brp_bewoning_client.models.bewoning_met_periode import BewoningMetPeriode

# TODO update the JSON string below
json = "{}"
# create an instance of BewoningMetPeriode from a JSON string
bewoning_met_periode_instance = BewoningMetPeriode.from_json(json)
# print the JSON string representation of the object
print(BewoningMetPeriode.to_json())

# convert the object into a dict
bewoning_met_periode_dict = bewoning_met_periode_instance.to_dict()
# create an instance of BewoningMetPeriode from a dict
bewoning_met_periode_from_dict = BewoningMetPeriode.from_dict(bewoning_met_periode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


