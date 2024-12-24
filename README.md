# brp-bewoning-client
API voor het raadplegen van de (historische) bewoning van een adres.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.1.0
- Package version: 1.0.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/BRP-API/Haal-Centraal-BRP-bewoning](https://github.com/BRP-API/Haal-Centraal-BRP-bewoning)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import brp_bewoning_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import brp_bewoning_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import brp_bewoning_client
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
    except ApiException as e:
        print("Exception when calling BewoningApi->bewoningen: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BewoningApi* | [**bewoningen**](docs/BewoningApi.md#bewoningen) | **POST** /bewoningen | Raadplegen van bewoningen


## Documentation For Models

 - [AbstractDatum](docs/AbstractDatum.md)
 - [BadRequestFoutbericht](docs/BadRequestFoutbericht.md)
 - [Bewoner](docs/Bewoner.md)
 - [Bewoning](docs/Bewoning.md)
 - [BewoningMetPeildatum](docs/BewoningMetPeildatum.md)
 - [BewoningMetPeriode](docs/BewoningMetPeriode.md)
 - [BewoningenQuery](docs/BewoningenQuery.md)
 - [BewoningenQueryResponse](docs/BewoningenQueryResponse.md)
 - [DatumOnbekend](docs/DatumOnbekend.md)
 - [Foutbericht](docs/Foutbericht.md)
 - [GeboorteBasis](docs/GeboorteBasis.md)
 - [InvalidParam](docs/InvalidParam.md)
 - [JaarDatum](docs/JaarDatum.md)
 - [JaarMaandDatum](docs/JaarMaandDatum.md)
 - [Naam](docs/Naam.md)
 - [Periode](docs/Periode.md)
 - [VolledigeDatum](docs/VolledigeDatum.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




