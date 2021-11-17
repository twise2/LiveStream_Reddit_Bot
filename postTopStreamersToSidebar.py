from twitch.api_calls import get_top_twitch_streamers
from reddit.api_calls import set_streamers_sidebar_widget, set_streamers_sidebar_widget_for_old_reddit
from facebook.scrape_calls import get_top_facebook_streamers
import json

top_twitch_streamers = get_top_twitch_streamers()
top_facebook_streamers = get_top_facebook_streamers()

top_streams = top_twitch_streamers + top_facebook_streamers
top_streams = sorted(top_streams, key=lambda d: int(d['viewers']), reverse=True)
set_streamers_sidebar_widget(top_streams)
set_streamers_sidebar_widget_for_old_reddit(top_streams)


