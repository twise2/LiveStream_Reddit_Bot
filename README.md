# wololoBot
A small bot to interact with the reddit API. Get top viewers for a game and update the sidebar widget.

## TO USE

### Create a new widget with the shortname of "LiveStreams" on your subreddit

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
