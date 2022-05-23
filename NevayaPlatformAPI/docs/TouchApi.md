# swagger_client.TouchApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_touch_token**](TouchApi.md#post_touch_token) | **POST** /touch/token | Get a token to use in Touch API

# **post_touch_token**
> InlineResponse20029 post_touch_token(body=body)

Get a token to use in Touch API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TouchApi(swagger_client.ApiClient(configuration))
body = swagger_client.TouchTokenBody() # TouchTokenBody | At least one of `reservation_id` or `room_id` is required. If `reservation_id` is ommitted then the main reservation, if it exists, will be used for the token. (optional)

try:
    # Get a token to use in Touch API
    api_response = api_instance.post_touch_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TouchApi->post_touch_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TouchTokenBody**](TouchTokenBody.md)| At least one of &#x60;reservation_id&#x60; or &#x60;room_id&#x60; is required. If &#x60;reservation_id&#x60; is ommitted then the main reservation, if it exists, will be used for the token. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

