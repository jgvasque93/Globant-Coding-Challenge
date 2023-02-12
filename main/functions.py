from flask import  request
import requests
import json

#theaudiodb's endpoint links
endpoint_api_music_info='https://www.theaudiodb.com/api/v1/json/2/search.php?s='
endpoint_api_music_discography='https://theaudiodb.com/api/v1/json/2/discography.php?s='

#Handler of function error internal
def function_error(error):
	context={
	'message':error,
	'status':500
	}
	return context

#function to get  /artists
def get_data_artist():
    args_name = request.args.get('name')
    if(args_name is None or args_name==''):
        return function_error('parameter name  null or blank')
    res=requests.get(f'{endpoint_api_music_info}{args_name}')
    try:
        json_artist=res.json()
    except Exception as e:
        return function_error(f'error calling api {endpoint_api_music_info}{args_name}')
    
    info_artist=json_artist['artists'][0]
    res=requests.get(f'{endpoint_api_music_discography}{args_name}')
    try:
        json_album=res.json()['album']
    except Exception as e:
        return function_error(f'error calling api {endpoint_api_music_discography}{args_name}')
    
    list_discography=[{'album':x['strAlbum'],'year':x['intYearReleased']}for x in json_album]
    
    context={
    	'artist':str(info_artist['strArtist']),
    	'style':str(info_artist['strStyle']),
    	'mood':str(info_artist['strMood']),
    	'country':str(info_artist['strCountry']),
    	'discography':list_discography
    }
    return context

