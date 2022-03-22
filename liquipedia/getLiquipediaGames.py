import pywikibot
from pywikibot import family
from pywikibot.scripts.generate_family_file import FamilyFileGenerator
from bs4 import BeautifulSoup
import time
import re
import json
import datetime

# importing date class from datetime module
# creating the date object of today's date
tournamentDetails = []
liquipedia_rate_limit_seconds = 2 #https://liquipedia.net/api-terms-of-use

#try to connect to aoe
try:
    site = pywikibot.Site('en', 'aoe')  # The site we want to run our bot on
#otherwise create the family and connect
except:
    FamilyFileGenerator('https://liquipedia.net/ageofempires', 'aoe').run()
    site = pywikibot.Site('en', 'aoe')  # The site we want to run our bot on



def getLiquipediaGamesForToday():
    todays_date = datetime.date.today()
    this_year=todays_date.year
    tournamentCollections = [{'tier': 'A', 'page': 'Age_of_Empires_II/A-Tier_Tournaments'}, {'tier': 'A', 'page':'Age_of_Empires_II/S-Tier_Tournaments'}]
    #get the loaded page
    for collection in tournamentCollections:
        time.sleep(liquipedia_rate_limit_seconds) #liquipedia rate limits to one call per two seconds so let's not F that up
        pageString = collection['page']
        page = pywikibot.Page(site, f'{pageString}#{this_year}')
        soup = BeautifulSoup(page._get_parsed_page(), 'lxml')

        #find the tournament dates
        for tournament in soup.find_all("div", {"class": "divTable table-full-width tournament-card"}):
            tournamentName = ''
            try:
                #get the date of the tournament
                dateRangeString = tournament.find('div', {'class' : 'divCell EventDetails Date Header'}).text

                #if the date is not a single day
                if('-' in dateRangeString):
                    [start, end] = dateRangeString.split('-', 1)
                    [end, endYear] = end.split(',')
                    #handle if fall over year
                    if(',' in start):
                        [start, startYear] = start.split(',')
                    else:
                        startYear = endYear
                #else a one day tournament
                else:
                    [start, startYear] = dateRangeString.split(',')
                    [end, endYear] = [start, startYear]

                [start, end, startYear, endYear] = [start.strip(), end.strip(), startYear.strip(), endYear.strip()]


                #handle geenral logic after
                if(' ' in start):
                    [startMonth, startDay] = start.split(' ')
                else:
                    startDay = start

                if(' ' in end):
                    [endMonth, endDay] = end.split(' ')
                else:
                    endDay = end
                    endMonth = startMonth

                endMonthNumber = int(datetime.datetime.strptime(endMonth if endMonth else startMonth, '%b').month)
                startMonthNumber = int(datetime.datetime.strptime(startMonth if startMonth else endMonth, '%b').month)
                startDate = datetime.datetime(year=int(startYear), month=int(startMonthNumber), day=int(startDay))
                endDate = datetime.datetime(year=int(endYear), month=int(endMonthNumber), day=int(endDay))
                #get the name of the tournament
                name = tournament.find('b').text
                #append the tier and other information
                tournamentDetails.append({'name': name
                                          , 'tier': collection['tier']
                                          , 'startDate': startDate
                                          , 'endDate': endDate
                                        })

            except Exception as e:
                continue

    tournamentsLiveToday = [tournament for tournament in tournamentDetails if tournament['startDate'] <= datetime.datetime.now() <= tournament['endDate']]
    print('type', type(tournamentsLiveToday))
    return json.dumps(tournamentsLiveToday, indent=4, sort_keys=True, default=str)

