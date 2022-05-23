# swagger_client.RoomControlApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_room_control_info**](RoomControlApi.md#get_room_control_info) | **GET** /room-control/info | Room control info

# **get_room_control_info**
> InlineResponse20023 get_room_control_info(room_id)

Room control info

Find out what's available in the room and who the provider is.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoomControlApi(swagger_client.ApiClient(configuration))
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID

try:
    # Room control info
    api_response = api_instance.get_room_control_info(room_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomControlApi->get_room_control_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | [**str**](.md)| The room ID | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

