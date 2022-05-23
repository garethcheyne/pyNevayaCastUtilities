# swagger_client.ReservationsApi

All URIs are relative to *https://platform-api.services.nevaya.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_reservations**](ReservationsApi.md#delete_reservations) | **DELETE** /reservations | Delete reservation(s)
[**get_account_profiles**](ReservationsApi.md#get_account_profiles) | **GET** /account-profiles | Get a list of available account profiles
[**get_reservations**](ReservationsApi.md#get_reservations) | **GET** /reservations | Get reservations
[**get_reservations_id**](ReservationsApi.md#get_reservations_id) | **GET** /reservations/{id} | Retrieve a reservation
[**post_get_reservations**](ReservationsApi.md#post_get_reservations) | **POST** /reservations | Get reservations
[**post_reservations**](ReservationsApi.md#post_reservations) | **POST** /reservations/create | Check a guest into a room
[**put_reservations_id**](ReservationsApi.md#put_reservations_id) | **PUT** /reservations/{id} | Update a reservation

# **delete_reservations**
> delete_reservations(reservation_id=reservation_id, guest_id=guest_id)

Delete reservation(s)

Check a guest out of a room by deleting the reservation. Specifying `guest_id` checks that guest out of all rooms they currently have a reservation for. `reservation_id` or `guest_id` is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReservationsApi(swagger_client.ApiClient(configuration))
reservation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The reservation ID to delete (optional)
guest_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The guest ID (optional)

try:
    # Delete reservation(s)
    api_instance.delete_reservations(reservation_id=reservation_id, guest_id=guest_id)
except ApiException as e:
    print("Exception when calling ReservationsApi->delete_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | [**str**](.md)| The reservation ID to delete | [optional] 
 **guest_id** | [**str**](.md)| The guest ID | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_profiles**
> InlineResponse20036 get_account_profiles(company_id=company_id)

Get a list of available account profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReservationsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The company ID (optional)

try:
    # Get a list of available account profiles
    api_response = api_instance.get_account_profiles(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationsApi->get_account_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company ID | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations**
> InlineResponse200 get_reservations(site_id=site_id, room_id=room_id, guest_id=guest_id, room_name_cont=room_name_cont, reservation_number=reservation_number, room_name_eq=room_name_eq, guest_first_name_eq=guest_first_name_eq, guest_first_name_cont=guest_first_name_cont, guest_last_name_cont=guest_last_name_cont, guest_last_name_eq=guest_last_name_eq, room_ids=room_ids, guest_ids=guest_ids, page=page, per_page=per_page, pms_id=pms_id, pms_ids=pms_ids)

Get reservations

Get all the reservations matching the specified filters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReservationsApi(swagger_client.ApiClient(configuration))
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | May be ignored depending on user access rights, for example if the user only has access to a single site that sites' ID will be used (optional)
room_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The room ID (optional)
guest_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The guest ID (optional)
room_name_cont = 'room_name_cont_example' # str | The room name contains the value (optional)
reservation_number = 'reservation_number_example' # str | Reservation number usually assigned by the PMS (optional)
room_name_eq = 'room_name_eq_example' # str | The room name matches the value exactly (optional)
guest_first_name_eq = 'guest_first_name_eq_example' # str | The guests first name matches the value exactly (optional)
guest_first_name_cont = 'guest_first_name_cont_example' # str | The guests first name contains the value (optional)
guest_last_name_cont = 'guest_last_name_cont_example' # str | The guests last name contains the value (optional)
guest_last_name_eq = 'guest_last_name_eq_example' # str | The guests last name matches the value exactly (optional)
room_ids = 'room_ids_example' # str | Comma separated list of Room IDs (optional)
guest_ids = 'guest_ids_example' # str | Comma separated list of Guest IDs (optional)
page = 56 # int | Required page number in paginated results (optional)
per_page = 25 # int | Number of results per page (optional) (default to 25)
pms_id = 'pms_id_example' # str | ID assigned by the PMS (optional)
pms_ids = 'pms_ids_example' # str | Comma separated list of PMS IDs (optional)

try:
    # Get reservations
    api_response = api_instance.get_reservations(site_id=site_id, room_id=room_id, guest_id=guest_id, room_name_cont=room_name_cont, reservation_number=reservation_number, room_name_eq=room_name_eq, guest_first_name_eq=guest_first_name_eq, guest_first_name_cont=guest_first_name_cont, guest_last_name_cont=guest_last_name_cont, guest_last_name_eq=guest_last_name_eq, room_ids=room_ids, guest_ids=guest_ids, page=page, per_page=per_page, pms_id=pms_id, pms_ids=pms_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationsApi->get_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| May be ignored depending on user access rights, for example if the user only has access to a single site that sites&#x27; ID will be used | [optional] 
 **room_id** | [**str**](.md)| The room ID | [optional] 
 **guest_id** | [**str**](.md)| The guest ID | [optional] 
 **room_name_cont** | **str**| The room name contains the value | [optional] 
 **reservation_number** | **str**| Reservation number usually assigned by the PMS | [optional] 
 **room_name_eq** | **str**| The room name matches the value exactly | [optional] 
 **guest_first_name_eq** | **str**| The guests first name matches the value exactly | [optional] 
 **guest_first_name_cont** | **str**| The guests first name contains the value | [optional] 
 **guest_last_name_cont** | **str**| The guests last name contains the value | [optional] 
 **guest_last_name_eq** | **str**| The guests last name matches the value exactly | [optional] 
 **room_ids** | **str**| Comma separated list of Room IDs | [optional] 
 **guest_ids** | **str**| Comma separated list of Guest IDs | [optional] 
 **page** | **int**| Required page number in paginated results | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 25]
 **pms_id** | **str**| ID assigned by the PMS | [optional] 
 **pms_ids** | **str**| Comma separated list of PMS IDs | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations_id**
> InlineResponse2002 get_reservations_id(id)

Retrieve a reservation

Get the specified reservation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReservationsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource

try:
    # Retrieve a reservation
    api_response = api_instance.get_reservations_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationsApi->get_reservations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the resource | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_reservations**
> InlineResponse200 post_get_reservations(body=body)

Get reservations

Option to use post in case query would exceed the GET size limits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReservationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReservationsBody() # ReservationsBody |  (optional)

try:
    # Get reservations
    api_response = api_instance.post_get_reservations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationsApi->post_get_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReservationsBody**](ReservationsBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations**
> InlineResponse2002 post_reservations(body=body)

Check a guest into a room

Create a reservation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReservationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReservationForm() # ReservationForm | Requires either a guest ID or the guests first and last names. Automatically creates a guest if no matching guests are found. (optional)

try:
    # Check a guest into a room
    api_response = api_instance.post_reservations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationsApi->post_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReservationForm**](ReservationForm.md)| Requires either a guest ID or the guests first and last names. Automatically creates a guest if no matching guests are found. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reservations_id**
> InlineResponse2002 put_reservations_id(id, body=body)

Update a reservation

Update the specified reservation. Partial updates are supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReservationsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource
body = swagger_client.ReservationForm() # ReservationForm |  (optional)

try:
    # Update a reservation
    api_response = api_instance.put_reservations_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationsApi->put_reservations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the resource | 
 **body** | [**ReservationForm**](ReservationForm.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

