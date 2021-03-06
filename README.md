# LiveStream_Reddit_Bot
Get top twitch and facebook stream viewers for a game and update the sidebar widget and old reddit sidebar to show your community where to watch.

## TO USE

### Create a new widget with the 'Widget title' of "LiveStreams" on your subreddit
```
LiveStreams
```

### For old reddit. Add the below lines to the sidebar. If the old sidebar does not exist it will fail. The live streams will be populated in these lines.
```
######Live Streams
[](#startmarker)
**No streams are currently live.**
[](#endmarker)
```

This can be changed as well, but default to the name above. The POST API endpoint is broken, so you need to manually create the widget to be modified.


### Set up credentials in .example.env

*For twitch credentials reference here: https://dev.twitch.tv/docs/authentication* <br/>
*For reddit credentials reference here and create an app: https://www.reddit.com/prefs/apps/* <br/>
```
source .example.env
```

### Install conda 
```
https://docs.conda.io/en/latest/miniconda.html
```

### Setup env
```
conda env create -f environment.yml -n wololoBot
conda activate wololoBot
```

### Run script
```
python postTopStreamersToSidebar.py
```
