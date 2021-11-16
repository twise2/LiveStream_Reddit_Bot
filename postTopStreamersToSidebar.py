from twitch.api_calls import get_top_twitch_streamers
from reddit.api_calls import get_current_widgets
from facebook.scrape_calls import get_top_facebook_streamers
import json

top_twitch_streamers = get_top_twitch_streamers()
top_facebook_streamers = get_top_facebook_streamers()

top_streams = top_twitch_streamers + top_facebook_streamers
top_streams = sorted(top_streams, key=lambda d: int(d['viewers']), reverse=True) 
print(top_streams[0:10])
#print(json.dumps(get_current_widgets(), indent=2))


