import requests
import praw
import json
import os

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
USER_NAME = os.getenv('REDDIT_USER_NAME')
PASSWORD = os.environ.get('REDDIT_PASSWORD')
SECRET_TOKEN=os.environ.get('REDDIT_SECRET_TOKEN')
PERSONAL_USER_SCRIPT=os.environ.get('REDDIT_PERSONAL_USER_SCRIPT')


def get_praw_connection():
    reddit = praw.Reddit(client_id=PERSONAL_USER_SCRIPT, client_secret=SECRET_TOKEN, password=PASSWORD, user_agent='wololoBot', username=USER_NAME)
    return reddit

def get_auth_headers():
    auth = requests.auth.HTTPBasicAuth(PERSONAL_USER_SCRIPT, SECRET_TOKEN)
    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': USER_NAME,
            'password': PASSWORD}
    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'wololoBot'}
    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    return headers


