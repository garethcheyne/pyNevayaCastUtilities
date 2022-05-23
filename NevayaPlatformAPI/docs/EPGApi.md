# swagger_client.EPGApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_epg_now_and_next**](EPGApi.md#get_epg_now_and_next) | **GET** /epg/now-and-next | Get the programmes that are on now and next
[**get_epg_programmes**](EPGApi.md#get_epg_programmes) | **GET** /epg/data | Get EPG data

# **get_epg_now_and_next**
> list[InlineResponse20027] get_epg_now_and_next(epg_ids)

Get the programmes that are on now and next

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EPGApi(swagger_client.ApiClient(configuration))
epg_ids = 'epg_ids_example' # str | Comma separated list of channel EPG IDs

try:
    # Get the programmes that are on now and next
    api_response = api_instance.get_epg_now_and_next(epg_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EPGApi->get_epg_now_and_next: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epg_ids** | **str**| Comma separated list of channel EPG IDs | 

### Return type

[**list[InlineResponse20027]**](InlineResponse20027.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_epg_programmes**
> list[InlineResponse20026] get_epg_programmes(epg_ids, hours=hours, offset=offset)

Get EPG data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EPGApi(swagger_client.ApiClient(configuration))
epg_ids = 'epg_ids_example' # str | Comma separated list of channel EPG IDs
hours = 3 # int | How many hours of programming information required (optional) (default to 3)
offset = 0 # int | How many hours into the future should the programming information start (optional) (default to 0)

try:
    # Get EPG data
    api_response = api_instance.get_epg_programmes(epg_ids, hours=hours, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EPGApi->get_epg_programmes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epg_ids** | **str**| Comma separated list of channel EPG IDs | 
 **hours** | **int**| How many hours of programming information required | [optional] [default to 3]
 **offset** | **int**| How many hours into the future should the programming information start | [optional] [default to 0]

### Return type

[**list[InlineResponse20026]**](InlineResponse20026.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

