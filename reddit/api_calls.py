from reddit.auth import get_auth_headers
import os
import requests
SUBREDDIT=os.environ.get('SUBREDDIT')

def get_current_widgets():
    headers = get_auth_headers()
    # while the token is valid (~2 hours) we just add headers=headers to our requests
    response = requests.get(f'https://oauth.reddit.com/r/{SUBREDDIT}/api/widgets', headers=headers)
    return response.json()

