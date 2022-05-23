# swagger_client.TVApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tv_receivers**](TVApi.md#get_tv_receivers) | **GET** /tv/receivers | Get receivers
[**get_tv_receivers_embeddable_remote**](TVApi.md#get_tv_receivers_embeddable_remote) | **GET** /tv/receivers/embeddable-remote | Get a link to an application that can be displayed in an iframe
[**get_tv_receivers_id_applications**](TVApi.md#get_tv_receivers_id_applications) | **GET** /tv/receivers/applications | Get a list of applications available to the receiver
[**get_tv_receivers_id_channels**](TVApi.md#get_tv_receivers_id_channels) | **GET** /tv/receivers/channels | Get all channels available to a receiver
[**get_tv_receivers_id_data**](TVApi.md#get_tv_receivers_id_data) | **GET** /tv/receivers/data | Get all the data for a receiver
[**get_tv_receivers_id_movies**](TVApi.md#get_tv_receivers_id_movies) | **GET** /tv/receivers/movies | Get all movies available to the receiver
[**get_tv_receivers_id_sources**](TVApi.md#get_tv_receivers_id_sources) | **GET** /tv/receivers/sources | Get external sources for a receiver
[**get_tv_receivers_id_videos**](TVApi.md#get_tv_receivers_id_videos) | **GET** /tv/receivers/videos | Get videos for a receiver
[**post_tv_receivers**](TVApi.md#post_tv_receivers) | **POST** /tv/receivers | Get receivers
[**post_tv_receivers_control**](TVApi.md#post_tv_receivers_control) | **POST** /tv/receivers/control | Control multiple receivers
[**post_tv_receivers_id_applications_close**](TVApi.md#post_tv_receivers_id_applications_close) | **POST** /tv/receivers/applications/close | Close the currently open application on the receiver(s)
[**post_tv_receivers_id_applications_open**](TVApi.md#post_tv_receivers_id_applications_open) | **POST** /tv/receivers/applications/open | Open an application on the receiver(s)
[**post_tv_receivers_id_channels_play**](TVApi.md#post_tv_receivers_id_channels_play) | **POST** /tv/receivers/channels/play | Change the channel on the receiver(s)
[**post_tv_receivers_id_movies_play**](TVApi.md#post_tv_receivers_id_movies_play) | **POST** /tv/receivers/movies/play | Play a movie on a receiver
[**post_tv_receivers_id_sources_exit**](TVApi.md#post_tv_receivers_id_sources_exit) | **POST** /tv/receivers/sources/exit | Exit the current external source on the receiver(s)
[**post_tv_receivers_id_sources_switch**](TVApi.md#post_tv_receivers_id_sources_switch) | **POST** /tv/receivers/sources/switch | Switch external source on the receiver(s)
[**post_tv_receivers_id_videos_play**](TVApi.md#post_tv_receivers_id_videos_play) | **POST** /tv/receivers/videos/play | Play a video on the receiver(s)
[**post_tv_receivers_pairing_codes**](TVApi.md#post_tv_receivers_pairing_codes) | **POST** /tv/receivers/pairing-codes | Get the pairing codes for the receiver(s)

# **get_tv_receivers**
> InlineResponse2006 get_tv_receivers(site_id=site_id, page=page, per_page=per_page, receiver_ids=receiver_ids, room_id=room_id, room_name_eq=room_name_eq, room_name_cont=room_name_cont)

Get receivers

Get the list of receivers (TVs, STBs etc)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
page = 56 # int | Required page number in paginated results (optional)
per_page = 25 # int | Number of results per page (optional) (default to 25)
receiver_ids = 'receiver_ids_example' # str | Comma separated list of receiver IDs (optional)
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)
room_name_eq = 'room_name_eq_example' # str | The room name matches the value exactly (optional)
room_name_cont = 'room_name_cont_example' # str | The room name contains the value (optional)

try:
    # Get receivers
    api_response = api_instance.get_tv_receivers(site_id=site_id, page=page, per_page=per_page, receiver_ids=receiver_ids, room_id=room_id, room_name_eq=room_name_eq, room_name_cont=room_name_cont)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **page** | **int**| Required page number in paginated results | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 25]
 **receiver_ids** | **str**| Comma separated list of receiver IDs | [optional] 
 **room_id** | [**str**](.md)| The room ID | [optional] 
 **room_name_eq** | **str**| The room name matches the value exactly | [optional] 
 **room_name_cont** | **str**| The room name contains the value | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_receivers_embeddable_remote**
> InlineResponse20028 get_tv_receivers_embeddable_remote(receiver_id, expires_at=expires_at, background=background, button=button)

Get a link to an application that can be displayed in an iframe

Returns a URL with an access token (JWT) for the specified receiver.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The receiver ID
expires_at = '2013-10-20T19:20:30+01:00' # datetime | When should the token expire (optional)
background = '#38373D' # str | Background colour (optional) (default to #38373D)
button = '#525257' # str | Button background colour, an appropriate text colour will be automatically chosen (optional) (default to #525257)

try:
    # Get a link to an application that can be displayed in an iframe
    api_response = api_instance.get_tv_receivers_embeddable_remote(receiver_id, expires_at=expires_at, background=background, button=button)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers_embeddable_remote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_id** | [**str**](.md)| The receiver ID | 
 **expires_at** | **datetime**| When should the token expire | [optional] 
 **background** | **str**| Background colour | [optional] [default to #38373D]
 **button** | **str**| Button background colour, an appropriate text colour will be automatically chosen | [optional] [default to #525257]

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_receivers_id_applications**
> InlineResponse20012 get_tv_receivers_id_applications(receiver_id)

Get a list of applications available to the receiver

These are pre-installed applications such as YouTube etc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The receiver ID

try:
    # Get a list of applications available to the receiver
    api_response = api_instance.get_tv_receivers_id_applications(receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers_id_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_id** | [**str**](.md)| The receiver ID | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_receivers_id_channels**
> InlineResponse2007 get_tv_receivers_id_channels(receiver_id)

Get all channels available to a receiver

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The receiver ID

try:
    # Get all channels available to a receiver
    api_response = api_instance.get_tv_receivers_id_channels(receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers_id_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_id** | [**str**](.md)| The receiver ID | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_receivers_id_data**
> InlineResponse20011 get_tv_receivers_id_data(receiver_id)

Get all the data for a receiver

Includes movies, channels, videos etc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The receiver ID

try:
    # Get all the data for a receiver
    api_response = api_instance.get_tv_receivers_id_data(receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers_id_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_id** | [**str**](.md)| The receiver ID | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_receivers_id_movies**
> InlineResponse2008 get_tv_receivers_id_movies(receiver_id)

Get all movies available to the receiver

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The receiver ID

try:
    # Get all movies available to the receiver
    api_response = api_instance.get_tv_receivers_id_movies(receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers_id_movies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_id** | [**str**](.md)| The receiver ID | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_receivers_id_sources**
> InlineResponse20010 get_tv_receivers_id_sources(receiver_id)

Get external sources for a receiver

Returns a list of defined external sources for the receiver, i.e. HDMI 1, HDMI 2 etc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The receiver ID

try:
    # Get external sources for a receiver
    api_response = api_instance.get_tv_receivers_id_sources(receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers_id_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_id** | [**str**](.md)| The receiver ID | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_receivers_id_videos**
> InlineResponse2009 get_tv_receivers_id_videos(receiver_id)

Get videos for a receiver

Get a list of unencrypted HLS streams associated with the receiver

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The receiver ID

try:
    # Get videos for a receiver
    api_response = api_instance.get_tv_receivers_id_videos(receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->get_tv_receivers_id_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_id** | [**str**](.md)| The receiver ID | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers**
> InlineResponse2006 post_tv_receivers(body=body)

Get receivers

Get the list of receivers (TVs, STBs etc). Returns the same as the `GET` version but by using `POST` it allows more filter options to be applied without hitting any limits on `GET` requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.TvReceiversBody() # TvReceiversBody |  (optional)

try:
    # Get receivers
    api_response = api_instance.post_tv_receivers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TvReceiversBody**](TvReceiversBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_control**
> post_tv_receivers_control(body=body)

Control multiple receivers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ReceiversControlBody()] # list[ReceiversControlBody] | Send multiple control operations to multiple receivers. `receiver_id` or `room_tag_id` is required, if both are provided then `room_tag_id` will be ignored. (optional)

try:
    # Control multiple receivers
    api_instance.post_tv_receivers_control(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ReceiversControlBody]**](ReceiversControlBody.md)| Send multiple control operations to multiple receivers. &#x60;receiver_id&#x60; or &#x60;room_tag_id&#x60; is required, if both are provided then &#x60;room_tag_id&#x60; will be ignored. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_id_applications_close**
> post_tv_receivers_id_applications_close(body=body)

Close the currently open application on the receiver(s)

Closes the current application (Youtube, Netflix etc) and returns the receiver to the home screen

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApplicationsCloseBody() # ApplicationsCloseBody | At least one of `receiver_id`, `room_tag_id` or a non empty list of receiver IDs is required (optional)

try:
    # Close the currently open application on the receiver(s)
    api_instance.post_tv_receivers_id_applications_close(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_id_applications_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsCloseBody**](ApplicationsCloseBody.md)| At least one of &#x60;receiver_id&#x60;, &#x60;room_tag_id&#x60; or a non empty list of receiver IDs is required | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_id_applications_open**
> post_tv_receivers_id_applications_open(body=body)

Open an application on the receiver(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApplicationsOpenBody() # ApplicationsOpenBody | At least one of `receiver_id`, `room_tag_id` or a non empty list of receiver IDs is required (optional)

try:
    # Open an application on the receiver(s)
    api_instance.post_tv_receivers_id_applications_open(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_id_applications_open: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsOpenBody**](ApplicationsOpenBody.md)| At least one of &#x60;receiver_id&#x60;, &#x60;room_tag_id&#x60; or a non empty list of receiver IDs is required | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_id_channels_play**
> post_tv_receivers_id_channels_play(body=body)

Change the channel on the receiver(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelsPlayBody() # ChannelsPlayBody | At least one of `receiver_id`, `room_tag_id` or a non empty list of receiver IDs is required (optional)

try:
    # Change the channel on the receiver(s)
    api_instance.post_tv_receivers_id_channels_play(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_id_channels_play: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelsPlayBody**](ChannelsPlayBody.md)| At least one of &#x60;receiver_id&#x60;, &#x60;room_tag_id&#x60; or a non empty list of receiver IDs is required | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_id_movies_play**
> post_tv_receivers_id_movies_play(body=body)

Play a movie on a receiver

Play a purchased movie on the receiver.   Requires `vod_accessible` to be true.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoviesPlayBody() # MoviesPlayBody | At least one of `receiver_id`, `room_tag_id` or a non empty list of receiver IDs is required (optional)

try:
    # Play a movie on a receiver
    api_instance.post_tv_receivers_id_movies_play(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_id_movies_play: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoviesPlayBody**](MoviesPlayBody.md)| At least one of &#x60;receiver_id&#x60;, &#x60;room_tag_id&#x60; or a non empty list of receiver IDs is required | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_id_sources_exit**
> post_tv_receivers_id_sources_exit(body=body)

Exit the current external source on the receiver(s)

Exits the current external source and returns the receiver to it's home screen

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.SourcesExitBody() # SourcesExitBody | At least one of `receiver_id`, `room_tag_id` or a non empty list of receiver IDs is required (optional)

try:
    # Exit the current external source on the receiver(s)
    api_instance.post_tv_receivers_id_sources_exit(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_id_sources_exit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourcesExitBody**](SourcesExitBody.md)| At least one of &#x60;receiver_id&#x60;, &#x60;room_tag_id&#x60; or a non empty list of receiver IDs is required | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_id_sources_switch**
> post_tv_receivers_id_sources_switch(body=body)

Switch external source on the receiver(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.SourcesSwitchBody() # SourcesSwitchBody | At least one of `receiver_id`, `room_tag_id` or a non empty list of receiver IDs is required (optional)

try:
    # Switch external source on the receiver(s)
    api_instance.post_tv_receivers_id_sources_switch(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_id_sources_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourcesSwitchBody**](SourcesSwitchBody.md)| At least one of &#x60;receiver_id&#x60;, &#x60;room_tag_id&#x60; or a non empty list of receiver IDs is required | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_id_videos_play**
> post_tv_receivers_id_videos_play(body=body)

Play a video on the receiver(s)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.VideosPlayBody() # VideosPlayBody | At least one of `receiver_id`, `room_tag_id` or a non empty list of receiver IDs is required (optional)

try:
    # Play a video on the receiver(s)
    api_instance.post_tv_receivers_id_videos_play(body=body)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_id_videos_play: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VideosPlayBody**](VideosPlayBody.md)| At least one of &#x60;receiver_id&#x60;, &#x60;room_tag_id&#x60; or a non empty list of receiver IDs is required | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tv_receivers_pairing_codes**
> InlineResponse20013 post_tv_receivers_pairing_codes(body=body)

Get the pairing codes for the receiver(s)

Optionally return a URL to the QR code image that matches the pairing code by setting `qr` to `true`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TVApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReceiversPairingcodesBody() # ReceiversPairingcodesBody |  (optional)

try:
    # Get the pairing codes for the receiver(s)
    api_response = api_instance.post_tv_receivers_pairing_codes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TVApi->post_tv_receivers_pairing_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceiversPairingcodesBody**](ReceiversPairingcodesBody.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

