from twitch.api_calls import get_top_twitch_streamers
from reddit.api_calls import get_current_widgets
import json

#top_twitch_streamsers = get_top_twitch_streamers()
#print(json.dumps(top_twitch_streamsers, indent=4))
print(json.dumps(get_current_widgets(), indent=2))
