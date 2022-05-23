# swagger_client.MaintenanceApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_maintenance_items**](MaintenanceApi.md#get_maintenance_items) | **GET** /maintenance/items | Get a list of available maintenance items
[**get_maintenance_requests**](MaintenanceApi.md#get_maintenance_requests) | **GET** /maintenance/requests | Get a list of maintenance requests
[**post_maintenance_requests**](MaintenanceApi.md#post_maintenance_requests) | **POST** /maintenance/requests | Create a maintenance request
[**put_maintenance_requests**](MaintenanceApi.md#put_maintenance_requests) | **PUT** /maintenance/requests | Update a maintenance request

# **get_maintenance_items**
> InlineResponse20030 get_maintenance_items(site_id=site_id, room_id=room_id)

Get a list of available maintenance items

`site_id` or `room_id` must be present, `room_id` will take precedence in the lookup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)

try:
    # Get a list of available maintenance items
    api_response = api_instance.get_maintenance_items(site_id=site_id, room_id=room_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->get_maintenance_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **room_id** | [**str**](.md)| The room ID | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_requests**
> InlineResponse20031 get_maintenance_requests(site_id=site_id, room_id=room_id, page=page, per_page=per_page)

Get a list of maintenance requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)
page = 56 # int | Required page number in paginated results (optional)
per_page = 25 # int | Number of results per page (optional) (default to 25)

try:
    # Get a list of maintenance requests
    api_response = api_instance.get_maintenance_requests(site_id=site_id, room_id=room_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->get_maintenance_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **room_id** | [**str**](.md)| The room ID | [optional] 
 **page** | **int**| Required page number in paginated results | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 25]

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_maintenance_requests**
> InlineResponse20033 post_maintenance_requests(body=body)

Create a maintenance request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))
body = swagger_client.MaintenanceRequestsBody1() # MaintenanceRequestsBody1 |  (optional)

try:
    # Create a maintenance request
    api_response = api_instance.post_maintenance_requests(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->post_maintenance_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceRequestsBody1**](MaintenanceRequestsBody1.md)|  | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_maintenance_requests**
> InlineResponse20032 put_maintenance_requests(body=body)

Update a maintenance request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))
body = swagger_client.MaintenanceRequestsBody() # MaintenanceRequestsBody |  (optional)

try:
    # Update a maintenance request
    api_response = api_instance.put_maintenance_requests(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->put_maintenance_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceRequestsBody**](MaintenanceRequestsBody.md)|  | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

