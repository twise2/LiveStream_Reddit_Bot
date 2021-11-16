import requests
import json
import os
import re
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chromedriver_autoinstaller.install()

GAME_ID = os.getenv('FACEBOOK_GAME_ID')
URL = 'https://www.facebook.com/gaming/browse/live/?game_id={FACEBOOK_GAME_ID}&s=VIEWERS&language=ALL_LANG'

chrome_options = Options()
chrome_options.add_argument("--headless") # Opens the browser up in background

with Chrome(options=chrome_options) as browser:
     browser.get(URL)
     html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')


#TODO: fix all this as it is not working at all
#for item in soup.find_all('div'):
#    #only check divs with one class
#    try:
#        if len(item["class"]) == 1:
#            results = item.find_all_next('a')
#            print('results', results)
#            #if two aria results
#            if len(results) == 2:
#                user = results[0]
#                game = results[1]
#                print('\n\n')
#                print('game', game)
#                print('user', user)
#                data = {
#                    'url': 1,
#                    'viewers':1,
#                    'user':1,
#                    'stream':1
#                }
#    except KeyError:
#        pass # or some other fallback action
#
