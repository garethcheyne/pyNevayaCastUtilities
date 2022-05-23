# Reservation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tv_rights** | **str** | TV rights for the guest. Mappings to common PMS  **FIAS**  TV rights map to the &#x60;TV&#x60; field of an &#x60;RE&#x60; Fias message in the following way:  | Nevaya    | Fias | Description                      | |-----------|------|----------------------------------| | unlimited | TU   | Unlimited pay channels (default) | | no_pay    | TM   | No pay movies                    | | no_adult  | TX   | No adult movies                  | | no_tv     | TN   | No TV rights                     | | [optional] [default to 'unlimited']
**minibar_rights** | **str** | Guests level of access to the minibar. Mappings to common PMS  **FIAS**  Minibar rights map to the &#x60;MR&#x60; field of an &#x60;RE&#x60; Fias message in the following way:  | Nevaya   | Fias | Description            | |----------|------|------------------------| | locked   | ML   | Lock minibar           | | unlocked | MU   | Unlock minibar         | | normal   | MN   | Minibar normal vending | | [optional] [default to 'normal']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

