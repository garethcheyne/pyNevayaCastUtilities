# swagger_client.GuestsApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_guests_id**](GuestsApi.md#delete_guests_id) | **DELETE** /guests/{id} | Delete a guest
[**get_guests**](GuestsApi.md#get_guests) | **GET** /guests | Get all guests
[**get_guests_id**](GuestsApi.md#get_guests_id) | **GET** /guests/{id} | Get a specific guest
[**post_guests**](GuestsApi.md#post_guests) | **POST** /guests | Get all guests
[**post_guests_create**](GuestsApi.md#post_guests_create) | **POST** /guests/create | Create a guest
[**put_guests_id**](GuestsApi.md#put_guests_id) | **PUT** /guests/{id} | Update a guest

# **delete_guests_id**
> delete_guests_id(id)

Delete a guest

Deletes a guest and any associated data such as reservations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GuestsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource

try:
    # Delete a guest
    api_instance.delete_guests_id(id)
except ApiException as e:
    print("Exception when calling GuestsApi->delete_guests_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the resource | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guests**
> InlineResponse20014 get_guests(page=page, per_page=per_page, first_name_eq=first_name_eq, last_name_eq=last_name_eq, first_name_cont=first_name_cont, last_name_cont=last_name_cont, company_id=company_id, pms_id=pms_id, company_ids=company_ids, pms_ids=pms_ids, ids=ids)

Get all guests

Get all the guests matching the filter. Guests are scoped to a company

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GuestsApi(swagger_client.ApiClient(configuration))
page = 56 # int | Required page number in paginated results (optional)
per_page = 25 # int | Number of results per page (optional) (default to 25)
first_name_eq = 'first_name_eq_example' # str | Guests first name equals the specified value (optional)
last_name_eq = 'last_name_eq_example' # str | Guest last name equals the specified value (optional)
first_name_cont = 'first_name_cont_example' # str | Guest first name contains the specified value (optional)
last_name_cont = 'last_name_cont_example' # str | Guest last name contains the specified value (optional)
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The company ID (optional)
pms_id = 'pms_id_example' # str | ID assigned by the PMS (optional)
company_ids = 'company_ids_example' # str | Comma separated list of company IDs (optional)
pms_ids = 'pms_ids_example' # str | Comma separated list of PMS IDs (optional)
ids = 'ids_example' # str | Comma separated list of guest IDs (optional)

try:
    # Get all guests
    api_response = api_instance.get_guests(page=page, per_page=per_page, first_name_eq=first_name_eq, last_name_eq=last_name_eq, first_name_cont=first_name_cont, last_name_cont=last_name_cont, company_id=company_id, pms_id=pms_id, company_ids=company_ids, pms_ids=pms_ids, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GuestsApi->get_guests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Required page number in paginated results | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 25]
 **first_name_eq** | **str**| Guests first name equals the specified value | [optional] 
 **last_name_eq** | **str**| Guest last name equals the specified value | [optional] 
 **first_name_cont** | **str**| Guest first name contains the specified value | [optional] 
 **last_name_cont** | **str**| Guest last name contains the specified value | [optional] 
 **company_id** | [**str**](.md)| The company ID | [optional] 
 **pms_id** | **str**| ID assigned by the PMS | [optional] 
 **company_ids** | **str**| Comma separated list of company IDs | [optional] 
 **pms_ids** | **str**| Comma separated list of PMS IDs | [optional] 
 **ids** | **str**| Comma separated list of guest IDs | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guests_id**
> InlineResponse20015 get_guests_id(id)

Get a specific guest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GuestsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource

try:
    # Get a specific guest
    api_response = api_instance.get_guests_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GuestsApi->get_guests_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the resource | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_guests**
> InlineResponse20014 post_guests(body=body)

Get all guests

Option to use post in case query would exceed the GET size limits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GuestsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GuestsBody() # GuestsBody |  (optional)

try:
    # Get all guests
    api_response = api_instance.post_guests(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GuestsApi->post_guests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GuestsBody**](GuestsBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_guests_create**
> InlineResponse20015 post_guests_create(body=body)

Create a guest

Normally guests will be created as part of the check in process or via a PMS.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GuestsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GuestsCreateBody() # GuestsCreateBody |  (optional)

try:
    # Create a guest
    api_response = api_instance.post_guests_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GuestsApi->post_guests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GuestsCreateBody**](GuestsCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_guests_id**
> InlineResponse20015 put_guests_id(id, body=body)

Update a guest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GuestsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource
body = swagger_client.GuestsIdBody() # GuestsIdBody | Update all or part of the guests data (optional)

try:
    # Update a guest
    api_response = api_instance.put_guests_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GuestsApi->put_guests_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the resource | 
 **body** | [**GuestsIdBody**](GuestsIdBody.md)| Update all or part of the guests data | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

