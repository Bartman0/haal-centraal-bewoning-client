# BewoningenQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bewoningen** | [**List[Bewoning]**](Bewoning.md) |  | [optional] 

## Example

```python
from brp_bewoning_client.models.bewoningen_query_response import BewoningenQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BewoningenQueryResponse from a JSON string
bewoningen_query_response_instance = BewoningenQueryResponse.from_json(json)
# print the JSON string representation of the object
print(BewoningenQueryResponse.to_json())

# convert the object into a dict
bewoningen_query_response_dict = bewoningen_query_response_instance.to_dict()
# create an instance of BewoningenQueryResponse from a dict
bewoningen_query_response_from_dict = BewoningenQueryResponse.from_dict(bewoningen_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


