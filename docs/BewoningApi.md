# brp_bewoning_client.BewoningApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bewoningen**](BewoningApi.md#bewoningen) | **POST** /bewoningen | Raadplegen van bewoningen


# **bewoningen**
> BewoningenQueryResponse bewoningen(bewoningen_query=bewoningen_query)

Raadplegen van bewoningen

Met de API kun je raadplegen:  **Bewoning:** welke personen (bewoners) een adresseerbaar object bewoonden op een opgegeven moment (peildatum) of welke samenstellingen van personen een adresseerbaar object bewoonden in een opgegeven periode. 

### Example


```python
import brp_bewoning_client
from brp_bewoning_client.models.bewoningen_query import BewoningenQuery
from brp_bewoning_client.models.bewoningen_query_response import BewoningenQueryResponse
from brp_bewoning_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = brp_bewoning_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with brp_bewoning_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brp_bewoning_client.BewoningApi(api_client)
    bewoningen_query = brp_bewoning_client.BewoningenQuery() # BewoningenQuery |  (optional)

    try:
        # Raadplegen van bewoningen
        api_response = api_instance.bewoningen(bewoningen_query=bewoningen_query)
        print("The response of BewoningApi->bewoningen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BewoningApi->bewoningen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bewoningen_query** | [**BewoningenQuery**](BewoningenQuery.md)|  | [optional] 

### Return type

[**BewoningenQueryResponse**](BewoningenQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zoekactie geslaagd  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**503** | Service Unavailable |  -  |
**0** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

