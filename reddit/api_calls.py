from reddit.auth import get_auth_headers
import os
import json
import requests
SUBREDDIT=os.environ.get('SUBREDDIT')
WIDGET_NAME=os.environ.get('WIDGET_NAME')


def set_streamers_sidebar_widget(top_streamers):
    headers = get_auth_headers()
    headers = {**headers, **{"Content-Type": "applications/json"}}
    widgets = requests.get(f'https://oauth.reddit.com/r/{SUBREDDIT}/api/widgets', headers=headers).json()['items']
    widget_id = None
    for widget in widgets.items():
        if ('shortName' in widget[1].keys() and widget[1]['shortName'] == WIDGET_NAME):
            widget_id = widget[0]#['id']

    data = build_stream_sidebar(top_streamers)
    if(widget_id):
        #post to is
        response = requests.put(f'https://oauth.reddit.com/r/{SUBREDDIT}/api/widget/{widget_id}', headers=headers, data=data)
    else:
        print('Failed to update stream as your widget with shortname: {WIDGET_NAME} was not found

def build_stream_sidebar(top_streamers):
    text = "Streamer | Lang | Views\n---------|----------|----------\n"
    for each in top_streamers:
        text+=f'🔴 [{each["streamer"]}]({each["link"]}) | EN | {each["viewers"]}\n'
    return json.dumps({
        "styles": { "headerColor": "#AABBCC" , "backgroundColor": "#AABBCC"},
        "kind": 'textarea',
        "shortName": WIDGET_NAME,
        "text": text
    })
