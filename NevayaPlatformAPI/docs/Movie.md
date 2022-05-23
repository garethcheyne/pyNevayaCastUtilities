# Movie

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**hd** | **bool** |  | [optional] 
**adult** | **bool** |  | [optional] 
**valid_for** | **int** | How many hours after purchase can a movie be watched for | [optional] 
**movie_languages** | [**list[MovieMovieLanguages]**](MovieMovieLanguages.md) | List of available audio languages for the movie:  | Code   | Language     |                                  | |--------|--------------|----------------------------------| | en | English      |                                  | | fr | Français     |                                  | | es | Español      |                                  | | de | Deutsch      |                                  | | it | Italiano     |                                  | | un | Undetermined | _Generally this will be English_ | | nl | Nederlands   |                                  | | [optional] 
**tmdb_id** | **str** | ID to be used with https://www.themoviedb.org/ | [optional] 
**short_description** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**genres** | **str** | List of genres for display purposes | [optional] 
**sub_genres** | **str** | List of sub genres for display purposes | [optional] 
**directors** | **str** | List of directors&#x27; names | [optional] 
**actors** | **str** | List of actors&#x27; names | [optional] 
**audio_languages** | **str** | Audio languages available | [optional] 
**rating** | **str** | BBFC rating | [optional] 
**runtime** | **int** | Movie runtime in minutes | [optional] 
**price** | **int** | Movie price in pence | [optional] 
**images** | [**MovieImages**](MovieImages.md) |  | [optional] 
**genre_ids** | **list[str]** |  | [optional] 
**sub_genre_ids** | **list[int]** |  | [optional] 
**dvd_release_date** | **date** | Date the movie was released on DVD | [optional] 
**valid_to** | **datetime** | If present, indicates the movie has been purchased and when access ends | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

