# wololoBot
A small bot to interact with the reddit API. Get top viewers and update the sidebar widget.

## TO USE

### Set up credentials in .example.env

*For twitch credential reference here: https://dev.twitch.tv/docs/authentication*
*For redit crential create a bot here: https://www.reddit.com/prefs/apps/*
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

### Run script (currently only prints)
```
python postTopStreamersToSidebar.py
```
