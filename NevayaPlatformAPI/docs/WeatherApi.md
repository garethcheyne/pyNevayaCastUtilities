# swagger_client.WeatherApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_weather_all**](WeatherApi.md#get_weather_all) | **GET** /weather/all | Get all the weather
[**get_weather_current**](WeatherApi.md#get_weather_current) | **GET** /weather/current | Get the current weather

# **get_weather_all**
> AllWeather get_weather_all(lat, lng, lang=lang)

Get all the weather

Get all the weather for the given latitude and longitude found in the weather section of the data endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))
lat = 1.2 # float | Latitude
lng = 1.2 # float | Longitude
lang = 'en' # str | The ISO 639-1 code of the language to return the data in (optional) (default to en)

try:
    # Get all the weather
    api_response = api_instance.get_weather_all(lat, lng, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->get_weather_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lng** | **float**| Longitude | 
 **lang** | **str**| The ISO 639-1 code of the language to return the data in | [optional] [default to en]

### Return type

[**AllWeather**](AllWeather.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weather_current**
> CurrentWeather get_weather_current(lat, lng, lang=lang)

Get the current weather

Get the current weather for the given latitude and longitude found in the weather section of the data endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))
lat = 1.2 # float | Latitude
lng = 1.2 # float | Longitude
lang = 'en' # str | The ISO 639-1 code of the language to return the data in (optional) (default to en)

try:
    # Get the current weather
    api_response = api_instance.get_weather_current(lat, lng, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->get_weather_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lng** | **float**| Longitude | 
 **lang** | **str**| The ISO 639-1 code of the language to return the data in | [optional] [default to en]

### Return type

[**CurrentWeather**](CurrentWeather.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

