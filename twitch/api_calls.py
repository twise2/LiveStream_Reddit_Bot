from twitch.auth import get_auth_headers
import requests
import os

GAME_ID = os.getenv('TWITCH_GAME_ID')

def get_top_twitch_streamers():
    headers = get_auth_headers()
    params = {
        'game_id': GAME_ID,
        'is_live' : True
    }
    response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
    return response.json()

