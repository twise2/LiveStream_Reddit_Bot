from reddit.auth import get_auth_headers, get_praw_connection
import os
import json
import requests

SUBREDDIT=os.environ.get('SUBREDDIT')
WIDGET_NAME=os.environ.get('WIDGET_NAME')



def set_streamers_sidebar_widget_for_old_reddit(top_streams):
    reddit = get_praw_connection()
    sidebar = reddit.subreddit(SUBREDDIT).wiki["config/sidebar"]
    sidebarContent = sidebar.content_md

    #split sidebar on livestream marker
    liveStreamInfo  = build_sidebar_markdown(top_streams)
    liveStreamStartString = '######Live Streams\n[](#startmarker)'
    liveStreamEndString = '[](#endmarker)'
    i = sidebarContent.find(liveStreamStartString)
    i2 = sidebarContent.find(liveStreamEndString)
    if(i != -1 and i2 !=-1):
        newSidebar = sidebarContent[:i + len(liveStreamStartString)] +  liveStreamInfo  + sidebarContent[i2:]
        sidebar.edit(content=newSidebar)
    else:
        print(f"Failed to find '{liveStreamStartString}' or '{liveStreamEndString}' in the old sidebar of r/{reddit}")

def set_streamers_sidebar_widget(top_streamers):
    headers = get_auth_headers()
    headers = {**headers, **{"Content-Type": "applications/json"}}
    widgets = requests.get(f'https://oauth.reddit.com/r/{SUBREDDIT}/api/widgets', headers=headers).json()['items']
    widget_id = None
    for widget in widgets.items():
        if ('shortName' in widget[1].keys() and widget[1]['shortName'] == WIDGET_NAME):
            widget_id = widget[0]#['id']

    data = build_sidebar_widget(top_streamers)
    if(widget_id):
        #post to is
        response = requests.put(f'https://oauth.reddit.com/r/{SUBREDDIT}/api/widget/{widget_id}', headers=headers, data=data)
    else:
        print('Failed to update stream as your widget with shortname: {WIDGET_NAME} was not found')

def build_sidebar_markdown(top_streamers):
    text = "Streamer | Lang | Views\n---------|----------|----------\n"
    for each in top_streamers:
        text+=f'🔴 [{each["streamer"]}]({each["link"]}) | {each["language"].upper()} | {each["viewers"]}\n'
    return text

def build_sidebar_widget(top_streamers):
    return json.dumps({
        "styles": { "headerColor": "#AABBCC" , "backgroundColor": "#AABBCC"},
        "kind": 'textarea',
        "shortName": WIDGET_NAME,
        "text": build_sidebar_markdown(top_streamers)
    })
