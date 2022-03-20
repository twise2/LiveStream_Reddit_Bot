import pywikibot
from pywikibot import family
from pywikibot.scripts.generate_family_file import FamilyFileGenerator
from bs4 import BeautifulSoup
import re
import json
import datetime

# importing date class from datetime module
# creating the date object of today's date
todays_date = datetime.date.today()
tournamentDetails = []

#try to connect to aoe
try:
    site = pywikibot.Site('en', 'aoe')  # The site we want to run our bot on
#otherwise create the family and connect
except:
    FamilyFileGenerator('https://liquipedia.net/ageofempires', 'aoe').run()
    site = pywikibot.Site('en', 'aoe')  # The site we want to run our bot on


this_year=todays_date.year
tournamentCollections = [{'tier': 'A', 'page': 'Age_of_Empires_II/A-Tier_Tournaments'}, {'tier': 'A', 'page':'Age_of_Empires_II/S-Tier_Tournaments'}]
#get the loaded page
for collection in tournamentCollections:
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
            startDate = datetime.datetime(year=int(startYear), month=int(startMonthNumber), day=int(startDay)).strftime("%m/%d/%Y")
            endDate = datetime.datetime(year=int(endYear), month=int(endMonthNumber), day=int(endDay)).strftime("%m/%d/%Y")
            #get the name of the tournament
            name = tournament.find('b').text
            #append the tier and other information
            tournamentDetails.append({'name': name
                                      , 'tier': collection['tier']
                                      , 'startDate': startDate
                                      , 'endDate': endDate
                                    })

        except Exception as e:
            print('error on tournament find', dateRangeString, e)
            print('\n\ndetails', tournament, '\n\n')
            continue

print('tournamentDetails', json.dumps(list(tournamentDetails), indent=2))
