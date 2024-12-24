# BewoningMetPeildatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peildatum** | **date** |  | 
**adresseerbaar_object_identificatie** | **str** | De identificatiecode van een adresseerbaar object uitgezonderd de standaardwaarde (0000000000000000)  | 

## Example

```python
from brp_bewoning_client.models.bewoning_met_peildatum import BewoningMetPeildatum

# TODO update the JSON string below
json = "{}"
# create an instance of BewoningMetPeildatum from a JSON string
bewoning_met_peildatum_instance = BewoningMetPeildatum.from_json(json)
# print the JSON string representation of the object
print(BewoningMetPeildatum.to_json())

# convert the object into a dict
bewoning_met_peildatum_dict = bewoning_met_peildatum_instance.to_dict()
# create an instance of BewoningMetPeildatum from a dict
bewoning_met_peildatum_from_dict = BewoningMetPeildatum.from_dict(bewoning_met_peildatum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


