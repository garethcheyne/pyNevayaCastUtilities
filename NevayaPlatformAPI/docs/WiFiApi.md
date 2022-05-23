# swagger_client.WiFiApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tariffs**](WiFiApi.md#get_tariffs) | **GET** /wifi/tariffs | Get the available tariffs
[**post_wifi_vouchers**](WiFiApi.md#post_wifi_vouchers) | **POST** /wifi/vouchers | Generate vouchers

# **get_tariffs**
> InlineResponse20034 get_tariffs(company_id=company_id)

Get the available tariffs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WiFiApi(swagger_client.ApiClient(configuration))
company_id = 'company_id_example' # str | Company ID. Defaults to the user company ID (optional)

try:
    # Get the available tariffs
    api_response = api_instance.get_tariffs(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WiFiApi->get_tariffs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Company ID. Defaults to the user company ID | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wifi_vouchers**
> InlineResponse20035 post_wifi_vouchers(body=body)

Generate vouchers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WiFiApi(swagger_client.ApiClient(configuration))
body = swagger_client.WifiVouchersBody() # WifiVouchersBody |  (optional)

try:
    # Generate vouchers
    api_response = api_instance.post_wifi_vouchers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WiFiApi->post_wifi_vouchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WifiVouchersBody**](WifiVouchersBody.md)|  | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

