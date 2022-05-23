# swagger_client.IdentityApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mac**](IdentityApi.md#get_mac) | **GET** /identity/mac | Get the MAC discovery URL

# **get_mac**
> InlineResponse20025 get_mac(site_id=site_id, room_id=room_id)

Get the MAC discovery URL

This returns a URL that can be used to discover the MAC address of the guest device. If the URL is present then performing a GET request from the device whose MAC address you want to find will return the following:  ```json {   \"data\": \"<mac address>\" } ```  If the MAC address cannot be found then a `404` message will be returned.  **Note**: A TV management or cast server appliance is required on site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.IdentityApi(swagger_client.ApiClient(configuration))
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)

try:
    # Get the MAC discovery URL
    api_response = api_instance.get_mac(site_id=site_id, room_id=room_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->get_mac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **room_id** | [**str**](.md)| The room ID | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

