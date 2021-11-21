from twitch.auth import get_auth_headers
import requests
import os

GAME_ID = os.getenv('TWITCH_GAME_ID')

def get_top_twitch_streamers():
    games = []
    headers = get_auth_headers()
    params = {
        'game_id': GAME_ID,
        'is_live' : True
    }
    try:
        response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
        for each in response.json()['data']:
            user_name = each['user_name']
            games.append({
                'link': f'https://www.twitch.tv/{user_name}',
                'streamer': user_name,
                'viewers': each['viewer_count'],
                'language' : each['language']
            })
        return games
    except Exception as e:
        print("Failed to request Twitch, exception:", str(e))
        return []





