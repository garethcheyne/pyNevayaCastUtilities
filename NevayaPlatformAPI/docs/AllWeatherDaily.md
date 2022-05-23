# AllWeatherDaily

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **int** | Time of the forecasted data, Unix, UTC | [optional] 
**sunrise** | **int** | Sunrise time, Unix, UTC | [optional] 
**sunset** | **int** | Sunset time, Unix, UTC | [optional] 
**temp** | [**AllWeatherTemp**](AllWeatherTemp.md) |  | [optional] 
**feels_like** | [**AllWeatherFeelsLike**](AllWeatherFeelsLike.md) |  | [optional] 
**pressure** | **float** | Atmospheric pressure on the sea level, hPa | [optional] 
**humidity** | **float** | Humidity, % | [optional] 
**dew_point** | **float** | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form, in Kelvin | [optional] 
**wind_speed** | **float** | Wind speed, in m/s | [optional] 
**wind_deg** | **float** | Wind direction, in degrees (meteorological) | [optional] 
**weather** | [**AllWeatherCurrentWeather**](AllWeatherCurrentWeather.md) |  | [optional] 
**clouds** | **float** | Cloudiness, % | [optional] 
**pop** | **float** | Probability of precipitation | [optional] 
**uvi** | **float** | Midday UV index | [optional] 
**icon** | **int** | Internal | [optional] 
**rain** | **float** | Rain volume, in mm | [optional] 
**snow** | **float** | Snow volume, in mm | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

