# swagger_client.RoomsApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rooms**](RoomsApi.md#get_rooms) | **GET** /rooms | Get rooms
[**get_rooms_id**](RoomsApi.md#get_rooms_id) | **GET** /rooms/{id} | Get a room
[**post_rooms**](RoomsApi.md#post_rooms) | **POST** /rooms | Get rooms
[**put_rooms_id**](RoomsApi.md#put_rooms_id) | **PUT** /rooms/{id} | Update a room

# **get_rooms**
> InlineResponse2003 get_rooms(site_id=site_id, page=page, per_page=per_page, name_cont=name_cont, name_eq=name_eq, devices=devices, room_ids=room_ids)

Get rooms

Get all the rooms matching the filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoomsApi(swagger_client.ApiClient(configuration))
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
page = 56 # int | Required page number in paginated results (optional)
per_page = 25 # int | Number of results per page (optional) (default to 25)
name_cont = 'name_cont_example' # str | Room name contains the value (optional)
name_eq = 'name_eq_example' # str | Room name equals the value (optional)
devices = true # bool | Include the associated devices with the room data (optional)
room_ids = 'room_ids_example' # str | Comma separated list of Room IDs (optional)

try:
    # Get rooms
    api_response = api_instance.get_rooms(site_id=site_id, page=page, per_page=per_page, name_cont=name_cont, name_eq=name_eq, devices=devices, room_ids=room_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsApi->get_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **page** | **int**| Required page number in paginated results | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 25]
 **name_cont** | **str**| Room name contains the value | [optional] 
 **name_eq** | **str**| Room name equals the value | [optional] 
 **devices** | **bool**| Include the associated devices with the room data | [optional] 
 **room_ids** | **str**| Comma separated list of Room IDs | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rooms_id**
> InlineResponse2004 get_rooms_id(id)

Get a room

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoomsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource

try:
    # Get a room
    api_response = api_instance.get_rooms_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsApi->get_rooms_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the resource | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rooms**
> InlineResponse2003 post_rooms(body=body)

Get rooms

Get all the rooms matching the filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoomsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoomsBody() # RoomsBody |  (optional)

try:
    # Get rooms
    api_response = api_instance.post_rooms(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsApi->post_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoomsBody**](RoomsBody.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_rooms_id**
> InlineResponse2005 put_rooms_id(id, body=body)

Update a room

Update a room

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RoomsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource
body = swagger_client.RoomStatus() # RoomStatus |  (optional)

try:
    # Update a room
    api_response = api_instance.put_rooms_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsApi->put_rooms_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the resource | 
 **body** | [**RoomStatus**](RoomStatus.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

