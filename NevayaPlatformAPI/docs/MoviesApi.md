# swagger_client.MoviesApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_guests_id_movies**](MoviesApi.md#get_guests_id_movies) | **GET** /movies/purchases | Get all the movies purchased
[**get_movies**](MoviesApi.md#get_movies) | **GET** /movies | Get the available movies
[**post_movies_purchases**](MoviesApi.md#post_movies_purchases) | **POST** /movies/purchases | Purchase a movie

# **get_guests_id_movies**
> InlineResponse20016 get_guests_id_movies(room_id=room_id, reservation_id=reservation_id, guest_id=guest_id)

Get all the movies purchased

Returns a list of all valid movies for the given `guest_id`, `reservation_id` or `room_id`.   At least one field is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MoviesApi(swagger_client.ApiClient(configuration))
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)
reservation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The reservation ID (optional)
guest_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The guest ID (optional)

try:
    # Get all the movies purchased
    api_response = api_instance.get_guests_id_movies(room_id=room_id, reservation_id=reservation_id, guest_id=guest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoviesApi->get_guests_id_movies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | [**str**](.md)| The room ID | [optional] 
 **reservation_id** | [**str**](.md)| The reservation ID | [optional] 
 **guest_id** | [**str**](.md)| The guest ID | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movies**
> InlineResponse20024 get_movies(site_id=site_id, room_id=room_id)

Get the available movies

Returns all the movies for the site or room. If `room_id` is specified then `site_id` is ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MoviesApi(swagger_client.ApiClient(configuration))
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)

try:
    # Get the available movies
    api_response = api_instance.get_movies(site_id=site_id, room_id=room_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoviesApi->get_movies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **room_id** | [**str**](.md)| The room ID | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_movies_purchases**
> InlineResponse20017 post_movies_purchases(body=body)

Purchase a movie

Purchase a movie

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MoviesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoviesPurchasesBody() # MoviesPurchasesBody | If purchase is made using `room_id` then the main guest will be used, the first guest checked into a room in the case of multiple reservations for a single room. Only one field is required, but if `room_id` is specified it will be ignored in preference to either the `guest_id` or `reservation_id`.

If there is already a valid purchase for the movie and guest then that will be returned.  (optional)

try:
    # Purchase a movie
    api_response = api_instance.post_movies_purchases(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoviesApi->post_movies_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoviesPurchasesBody**](MoviesPurchasesBody.md)| If purchase is made using &#x60;room_id&#x60; then the main guest will be used, the first guest checked into a room in the case of multiple reservations for a single room. Only one field is required, but if &#x60;room_id&#x60; is specified it will be ignored in preference to either the &#x60;guest_id&#x60; or &#x60;reservation_id&#x60;.

If there is already a valid purchase for the movie and guest then that will be returned.  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

