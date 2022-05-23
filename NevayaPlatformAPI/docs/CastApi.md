# swagger_client.CastApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cast_chromecasts**](CastApi.md#get_cast_chromecasts) | **GET** /cast/chromecasts | Get a list of chromecasts
[**get_cast_chromecasts_id**](CastApi.md#get_cast_chromecasts_id) | **GET** /cast/chromecasts/{chromecast_id} | Get a chromecast
[**get_cast_connections**](CastApi.md#get_cast_connections) | **GET** /cast/connections | Get all valid connections
[**post_cast_chromecasts**](CastApi.md#post_cast_chromecasts) | **POST** /cast/chromecasts | Get a list of chromecasts
[**post_cast_chromecasts_id_reboot**](CastApi.md#post_cast_chromecasts_id_reboot) | **POST** /cast/chromecasts/reboot | Reboot the chromecast(s)
[**post_cast_chromecasts_id_reset**](CastApi.md#post_cast_chromecasts_id_reset) | **POST** /cast/chromecasts/reset | Reset the chromecast(s)
[**post_cast_chromecasts_pairing_codes**](CastApi.md#post_cast_chromecasts_pairing_codes) | **POST** /cast/chromecasts/pairing-codes | Get the pairing codes for the chromecast(s)
[**post_cast_connections**](CastApi.md#post_cast_connections) | **POST** /cast/connections | Get all valid connections
[**post_cast_connections_connect**](CastApi.md#post_cast_connections_connect) | **POST** /cast/connections/connect | Connect a guest device
[**post_cast_connections_expire**](CastApi.md#post_cast_connections_expire) | **POST** /cast/connections/expire | Expire connections
[**put_cast_chromecasts_id**](CastApi.md#put_cast_chromecasts_id) | **PUT** /cast/chromecasts/{chromecast_id} | Update a chromecast

# **get_cast_chromecasts**
> InlineResponse20018 get_cast_chromecasts(page=page, per_page=per_page, room_name_eq=room_name_eq, room_name_cont=room_name_cont, site_id=site_id, room_ids=room_ids)

Get a list of chromecasts

Get a list of chromecasts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
page = 56 # int | Required page number in paginated results (optional)
per_page = 25 # int | Number of results per page (optional) (default to 25)
room_name_eq = 'room_name_eq_example' # str | The room name matches the value exactly (optional)
room_name_cont = 'room_name_cont_example' # str | The room name contains the value (optional)
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The site ID (optional)
room_ids = 'room_ids_example' # str | Comma separated list of Room IDs (optional)

try:
    # Get a list of chromecasts
    api_response = api_instance.get_cast_chromecasts(page=page, per_page=per_page, room_name_eq=room_name_eq, room_name_cont=room_name_cont, site_id=site_id, room_ids=room_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->get_cast_chromecasts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Required page number in paginated results | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 25]
 **room_name_eq** | **str**| The room name matches the value exactly | [optional] 
 **room_name_cont** | **str**| The room name contains the value | [optional] 
 **site_id** | [**str**](.md)| The site ID | [optional] 
 **room_ids** | **str**| Comma separated list of Room IDs | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cast_chromecasts_id**
> InlineResponse20019 get_cast_chromecasts_id(chromecast_id)

Get a chromecast

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
chromecast_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the chromecast

try:
    # Get a chromecast
    api_response = api_instance.get_cast_chromecasts_id(chromecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->get_cast_chromecasts_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chromecast_id** | [**str**](.md)| The ID of the chromecast | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cast_connections**
> InlineResponse20021 get_cast_connections(page=page, per_page=per_page, site_id=site_id, room_name_eq=room_name_eq, room_name_cont=room_name_cont, guest_first_name_eq=guest_first_name_eq, guest_last_name_eq=guest_last_name_eq, guest_first_name_cont=guest_first_name_cont, guest_last_name_cont=guest_last_name_cont, guest_id=guest_id, room_id=room_id, chromecast_id=chromecast_id, guest_ids=guest_ids, room_ids=room_ids, chromecast_ids=chromecast_ids)

Get all valid connections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
page = 56 # int | Required page number in paginated results (optional)
per_page = 25 # int | Number of results per page (optional) (default to 25)
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
room_name_eq = 'room_name_eq_example' # str | The room name matches the value exactly (optional)
room_name_cont = 'room_name_cont_example' # str | The room name contains the value (optional)
guest_first_name_eq = 'guest_first_name_eq_example' # str | The guests first name matches the value exactly (optional)
guest_last_name_eq = 'guest_last_name_eq_example' # str | The guests last name matches the value exactly (optional)
guest_first_name_cont = 'guest_first_name_cont_example' # str | The guests first name contains the value (optional)
guest_last_name_cont = 'guest_last_name_cont_example' # str | The guests last name contains the value (optional)
guest_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The guest ID (optional)
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)
chromecast_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The chromecast ID (optional)
guest_ids = 'guest_ids_example' # str | Comma separated list of Guest IDs (optional)
room_ids = 'room_ids_example' # str | Comma separated list of Room IDs (optional)
chromecast_ids = 'chromecast_ids_example' # str | Comma separated list of Chromecast IDs (optional)

try:
    # Get all valid connections
    api_response = api_instance.get_cast_connections(page=page, per_page=per_page, site_id=site_id, room_name_eq=room_name_eq, room_name_cont=room_name_cont, guest_first_name_eq=guest_first_name_eq, guest_last_name_eq=guest_last_name_eq, guest_first_name_cont=guest_first_name_cont, guest_last_name_cont=guest_last_name_cont, guest_id=guest_id, room_id=room_id, chromecast_id=chromecast_id, guest_ids=guest_ids, room_ids=room_ids, chromecast_ids=chromecast_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->get_cast_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Required page number in paginated results | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 25]
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **room_name_eq** | **str**| The room name matches the value exactly | [optional] 
 **room_name_cont** | **str**| The room name contains the value | [optional] 
 **guest_first_name_eq** | **str**| The guests first name matches the value exactly | [optional] 
 **guest_last_name_eq** | **str**| The guests last name matches the value exactly | [optional] 
 **guest_first_name_cont** | **str**| The guests first name contains the value | [optional] 
 **guest_last_name_cont** | **str**| The guests last name contains the value | [optional] 
 **guest_id** | [**str**](.md)| The guest ID | [optional] 
 **room_id** | [**str**](.md)| The room ID | [optional] 
 **chromecast_id** | [**str**](.md)| The chromecast ID | [optional] 
 **guest_ids** | **str**| Comma separated list of Guest IDs | [optional] 
 **room_ids** | **str**| Comma separated list of Room IDs | [optional] 
 **chromecast_ids** | **str**| Comma separated list of Chromecast IDs | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cast_chromecasts**
> InlineResponse20018 post_cast_chromecasts(body=body)

Get a list of chromecasts

Option to use post in case query would exceed the GET size limits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
body = swagger_client.CastChromecastsBody() # CastChromecastsBody |  (optional)

try:
    # Get a list of chromecasts
    api_response = api_instance.post_cast_chromecasts(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->post_cast_chromecasts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CastChromecastsBody**](CastChromecastsBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cast_chromecasts_id_reboot**
> post_cast_chromecasts_id_reboot(body=body)

Reboot the chromecast(s)

Reboot the specified chromecast(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChromecastsRebootBody() # ChromecastsRebootBody | Either `chromecast_id` is specified or a non empty `chromecast_ids` array is required. If both are specified then `chromecast_ids` is ignored (optional)

try:
    # Reboot the chromecast(s)
    api_instance.post_cast_chromecasts_id_reboot(body=body)
except ApiException as e:
    print("Exception when calling CastApi->post_cast_chromecasts_id_reboot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChromecastsRebootBody**](ChromecastsRebootBody.md)| Either &#x60;chromecast_id&#x60; is specified or a non empty &#x60;chromecast_ids&#x60; array is required. If both are specified then &#x60;chromecast_ids&#x60; is ignored | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cast_chromecasts_id_reset**
> post_cast_chromecasts_id_reset(body=body)

Reset the chromecast(s)

Load the Nevaya application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChromecastsResetBody() # ChromecastsResetBody | Either `chromecast_id` is specified or a non empty `chromecast_ids` array is required. If both are specified then `chromecast_ids` is ignored (optional)

try:
    # Reset the chromecast(s)
    api_instance.post_cast_chromecasts_id_reset(body=body)
except ApiException as e:
    print("Exception when calling CastApi->post_cast_chromecasts_id_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChromecastsResetBody**](ChromecastsResetBody.md)| Either &#x60;chromecast_id&#x60; is specified or a non empty &#x60;chromecast_ids&#x60; array is required. If both are specified then &#x60;chromecast_ids&#x60; is ignored | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cast_chromecasts_pairing_codes**
> InlineResponse20020 post_cast_chromecasts_pairing_codes(body=body)

Get the pairing codes for the chromecast(s)

Pairing codes expire so they must be fetched occasionally. Optionally return a QR code in SVG

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChromecastsPairingcodesBody() # ChromecastsPairingcodesBody |  (optional)

try:
    # Get the pairing codes for the chromecast(s)
    api_response = api_instance.post_cast_chromecasts_pairing_codes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->post_cast_chromecasts_pairing_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChromecastsPairingcodesBody**](ChromecastsPairingcodesBody.md)|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cast_connections**
> InlineResponse20021 post_cast_connections(body=body)

Get all valid connections

Option to use post in case query would exceed the GET size limits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
body = swagger_client.CastConnectionsBody() # CastConnectionsBody |  (optional)

try:
    # Get all valid connections
    api_response = api_instance.post_cast_connections(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->post_cast_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CastConnectionsBody**](CastConnectionsBody.md)|  | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cast_connections_connect**
> InlineResponse202 post_cast_connections_connect(body=body)

Connect a guest device

Create a connection between a guest device and a chromecast

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectionsConnectBody() # ConnectionsConnectBody | `guest_device_id` or `guest_device_mac` must be present.

`hours` can be specified as the number of hours before the connection is automatically expired, or `permanent` to ensure the connection is never automatically expired. Defaults to the configured value in the Nevaya Cast application.
 (optional)

try:
    # Connect a guest device
    api_response = api_instance.post_cast_connections_connect(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->post_cast_connections_connect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionsConnectBody**](ConnectionsConnectBody.md)| &#x60;guest_device_id&#x60; or &#x60;guest_device_mac&#x60; must be present.

&#x60;hours&#x60; can be specified as the number of hours before the connection is automatically expired, or &#x60;permanent&#x60; to ensure the connection is never automatically expired. Defaults to the configured value in the Nevaya Cast application.
 | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cast_connections_expire**
> post_cast_connections_expire(body=body)

Expire connections

All guest device connections that match the applied filter will be expired. No connections will be expired if there isn't at least one filter present.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectionsExpireBody() # ConnectionsExpireBody |  (optional)

try:
    # Expire connections
    api_instance.post_cast_connections_expire(body=body)
except ApiException as e:
    print("Exception when calling CastApi->post_cast_connections_expire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionsExpireBody**](ConnectionsExpireBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cast_chromecasts_id**
> InlineResponse20019 put_cast_chromecasts_id(chromecast_id, body=body)

Update a chromecast

Update a chromecast

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CastApi(swagger_client.ApiClient(configuration))
chromecast_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the chromecast
body = swagger_client.ChromecastsChromecastIdBody() # ChromecastsChromecastIdBody |  (optional)

try:
    # Update a chromecast
    api_response = api_instance.put_cast_chromecasts_id(chromecast_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastApi->put_cast_chromecasts_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chromecast_id** | [**str**](.md)| The ID of the chromecast | 
 **body** | [**ChromecastsChromecastIdBody**](ChromecastsChromecastIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

