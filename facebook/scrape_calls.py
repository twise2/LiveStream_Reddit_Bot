import requests
import json
import os
import re
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def get_top_facebook_streamers():
    try:
        chromedriver_autoinstaller.install()
        GAME_ID = os.getenv('FACEBOOK_GAME_ID')
        URL = f'https://www.facebook.com/gaming/browse/live/?game_id={GAME_ID}&s=VIEWERS&language=ALL_LANG'

        chrome_options = Options()
        chrome_options.add_argument("--headless") # Opens the browser up in background

        with Chrome(options=chrome_options) as browser:
             browser.get(URL)
             html = browser.page_source

        soup = BeautifulSoup(html, 'html.parser')
        games = []
        for item in soup.find_all('div', {"class": 'k4urcfbm'}):
            streamData = {}
            try:
                if len(item["class"]) == 1:

                    #print('item', item, '\n\n\n')
                    #get the data for the stream links
                    hrefs = item.find_all('a', href=True)
                    for each in hrefs:
                        link = each['href']
                        if('video' in link):
                            streamData['link'] = each['href']

                    #get the data for the streamer's name
                    regex = re.compile('(?<=www\.facebook\.com\/)(.*)(?=\/videos)')
                    if(streamData['link']):
                        streamData['streamer'] = regex.findall(streamData['link'])[0]

                    #get the data for the number of viewers
                    potential_numbers = item.find_all('span', {"class": ['a8c37x1j' 'ni8dbmo4', 'stjgntxs', 'l9j0dhe7', 'ltmttdrg', 'g0qnabr5']})
                    for each in potential_numbers:
                        if(each.text and each.text.isdigit()):
                            streamData['viewers'] = int(each.text)

                    streamData['language'] = ''
            except KeyError:
                pass # or some other fallback action

            if all (key in streamData for key in ["link", "viewers"]):
                games.append(streamData)
        return games
    except Exception as e:
        print("Failed to scrape facebook, exception:", str(e))
        return []
