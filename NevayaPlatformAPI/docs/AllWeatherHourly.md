# AllWeatherHourly

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **int** | Time of the forecasted data, Unix, UTC | [optional] 
**temp** | **float** | Temperature, in Kelvin | [optional] 
**feels_like** | **float** | This temperature parameter accounts for the human perception of weather, in Kelvin | [optional] 
**pressure** | **float** | Atmospheric pressure on the sea level, hPa | [optional] 
**humidity** | **float** | Humidity, % | [optional] 
**dew_point** | **float** | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form, in Kelvin | [optional] 
**clouds** | **float** | Cloudiness, % | [optional] 
**visibility** | **float** | Average visibility, in metres | [optional] 
**wind_speed** | **float** | Wind speed, in m/s | [optional] 
**wind_deg** | **float** | Wind direction, in degrees (meteorological) | [optional] 
**weather** | [**AllWeatherCurrentWeather**](AllWeatherCurrentWeather.md) |  | [optional] 
**pop** | **float** | Probability of precipitation | [optional] 
**icon** | **int** | Internal | [optional] 
**rain** | [**AllWeatherRain**](AllWeatherRain.md) |  | [optional] 
**snow** | [**AllWeatherSnow**](AllWeatherSnow.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

