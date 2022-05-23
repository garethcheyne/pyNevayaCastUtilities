# InlineResponse20022DataDevThermos

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_set_point** | **float** | Active setpoint is the current setpoint in the room. Which can be set-point forced by the Guest / Set-point forced from server in case of checked-out/Room is unoccupied. | [optional] 
**actual_temp** | **float** | Room current temperature | [optional] 
**fan_speed** | **str** | The current fan mode | [optional] 
**set_point** | **float** | Desired temperature set by the user | [optional] 
**thermostat_id** | **str** |  | [optional] 
**window_state** | **str** | Is the window open or closed | [optional] 
**valve_status** | **str** | The state has 3 parts &#x60;{valveValue}|{mode}|{valvePercentage}&#x60;  **ValveValue**: * ON * OFF  **Mode**: * Cooling * Heating  **ValvePercentage**: * 0-100 * N/A – in case the valve type is ON/OFF | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

