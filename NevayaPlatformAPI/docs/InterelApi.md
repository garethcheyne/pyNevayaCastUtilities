# swagger_client.InterelApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_room_control_interel_state**](InterelApi.md#get_room_control_interel_state) | **GET** /room-control/interel/state | Get the Interel room state
[**post_room_control_interel_set_blind_state**](InterelApi.md#post_room_control_interel_set_blind_state) | **POST** /room-control/interel/set-blind-state | Control the blinds in the room
[**post_room_control_interel_set_curtain_state**](InterelApi.md#post_room_control_interel_set_curtain_state) | **POST** /room-control/interel/set-curtain-state | Control the curtains in the room
[**post_room_control_interel_set_dnd_state**](InterelApi.md#post_room_control_interel_set_dnd_state) | **POST** /room-control/interel/set-dnd-state | Set the do not disturb state for the room
[**post_room_control_interel_set_fan_speed**](InterelApi.md#post_room_control_interel_set_fan_speed) | **POST** /room-control/interel/set-fan-speed | Set the fan speed for the room
[**post_room_control_interel_set_scene**](InterelApi.md#post_room_control_interel_set_scene) | **POST** /room-control/interel/set-scene | Set a scene
[**post_room_control_interel_set_temperature**](InterelApi.md#post_room_control_interel_set_temperature) | **POST** /room-control/interel/set-temperature | Set the temperature of a thermostat in the room
[**post_room_control_interel_toggle_light**](InterelApi.md#post_room_control_interel_toggle_light) | **POST** /room-control/interel/toggle-light | Toggle a light

# **get_room_control_interel_state**
> InlineResponse20022 get_room_control_interel_state(room_id)

Get the Interel room state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID

try:
    # Get the Interel room state
    api_response = api_instance.get_room_control_interel_state(room_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterelApi->get_room_control_interel_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | [**str**](.md)| The room ID | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_control_interel_set_blind_state**
> post_room_control_interel_set_blind_state(body=body)

Control the blinds in the room

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterelSetblindstateBody() # InterelSetblindstateBody |  (optional)

try:
    # Control the blinds in the room
    api_instance.post_room_control_interel_set_blind_state(body=body)
except ApiException as e:
    print("Exception when calling InterelApi->post_room_control_interel_set_blind_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterelSetblindstateBody**](InterelSetblindstateBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_control_interel_set_curtain_state**
> post_room_control_interel_set_curtain_state(body=body)

Control the curtains in the room

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterelSetcurtainstateBody() # InterelSetcurtainstateBody |  (optional)

try:
    # Control the curtains in the room
    api_instance.post_room_control_interel_set_curtain_state(body=body)
except ApiException as e:
    print("Exception when calling InterelApi->post_room_control_interel_set_curtain_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterelSetcurtainstateBody**](InterelSetcurtainstateBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_control_interel_set_dnd_state**
> post_room_control_interel_set_dnd_state(body=body)

Set the do not disturb state for the room

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterelSetdndstateBody() # InterelSetdndstateBody |  (optional)

try:
    # Set the do not disturb state for the room
    api_instance.post_room_control_interel_set_dnd_state(body=body)
except ApiException as e:
    print("Exception when calling InterelApi->post_room_control_interel_set_dnd_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterelSetdndstateBody**](InterelSetdndstateBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_control_interel_set_fan_speed**
> post_room_control_interel_set_fan_speed(body=body)

Set the fan speed for the room

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterelSetfanspeedBody() # InterelSetfanspeedBody |  (optional)

try:
    # Set the fan speed for the room
    api_instance.post_room_control_interel_set_fan_speed(body=body)
except ApiException as e:
    print("Exception when calling InterelApi->post_room_control_interel_set_fan_speed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterelSetfanspeedBody**](InterelSetfanspeedBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_control_interel_set_scene**
> post_room_control_interel_set_scene(body=body)

Set a scene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterelSetsceneBody() # InterelSetsceneBody |  (optional)

try:
    # Set a scene
    api_instance.post_room_control_interel_set_scene(body=body)
except ApiException as e:
    print("Exception when calling InterelApi->post_room_control_interel_set_scene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterelSetsceneBody**](InterelSetsceneBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_control_interel_set_temperature**
> post_room_control_interel_set_temperature(body=body)

Set the temperature of a thermostat in the room

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterelSettemperatureBody() # InterelSettemperatureBody |  (optional)

try:
    # Set the temperature of a thermostat in the room
    api_instance.post_room_control_interel_set_temperature(body=body)
except ApiException as e:
    print("Exception when calling InterelApi->post_room_control_interel_set_temperature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterelSettemperatureBody**](InterelSettemperatureBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_control_interel_toggle_light**
> post_room_control_interel_toggle_light(body=body)

Toggle a light

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterelApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterelTogglelightBody() # InterelTogglelightBody |  (optional)

try:
    # Toggle a light
    api_instance.post_room_control_interel_toggle_light(body=body)
except ApiException as e:
    print("Exception when calling InterelApi->post_room_control_interel_toggle_light: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterelTogglelightBody**](InterelTogglelightBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

