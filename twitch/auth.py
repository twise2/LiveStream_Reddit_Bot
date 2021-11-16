import requests
import json
import os

def get_auth_headers():
    CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
    CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')


    body = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        "grant_type": 'client_credentials'
    }
    print('body', body)
    r = requests.post('https://id.twitch.tv/oauth2/token', body)

    #data output
    keys = r.json();

    print('keys', keys)

    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': 'Bearer ' + keys['access_token']
    }

    return headers

    params = {
        'game_id': GAME_ID,
        'is_live' : True
    }

    print(headers)
    response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
    print(json.dumps(response.json(), indent=4))
