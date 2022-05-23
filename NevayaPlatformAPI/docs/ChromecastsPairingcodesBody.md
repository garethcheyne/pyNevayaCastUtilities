# ChromecastsPairingcodesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromecast_ids** | **list[str]** | An array of chromecast IDs | 
**colour** | **str** | The foreground colour of the QR code in HEX format | [optional] [default to '#000']
**fill** | **str** | The background colour of the QR code in HEX format | [optional] [default to '#fff']
**size** | **int** | Size of the image in px, always returns a square image | [optional] [default to 200]
**qr** | **OneOfchromecastsPairingcodesBodyQr** | Include the matching QR code image. If set to a string the string should be a URL. The QR code will point to &#x60;&lt;url&gt;?token&#x3D;&lt;token&gt;&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

