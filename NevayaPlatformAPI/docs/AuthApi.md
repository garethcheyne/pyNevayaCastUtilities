# swagger_client.AuthApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_auth**](AuthApi.md#post_auth) | **POST** /auth | Generate an auth token

# **post_auth**
> InlineResponse2001 post_auth(body=body)

Generate an auth token

Generate a JSON web token to be used to authenticate future API calls.  To get your API token go to https://portal.nevaya.net and sign in. Clicking the ![blue button](https://nevaya-site-data.s3-eu-west-1.amazonaws.com/openapi/api-key-button.png \"API key\") in the banner copies your API key to the clipboard. **Do not share your key with anyone.**  If you don't see the button it may be that your account doesn't have access to the API, please contact Nevaya support to have it added.   Generated tokens will expire automatically after six months, but can be expired at any time before then. Should that happen a `401` error will be returned from any protected API call, at which point a new token should be generated and used.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.AuthBody() # AuthBody |  (optional)

try:
    # Generate an auth token
    api_response = api_instance.post_auth(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthBody**](AuthBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

