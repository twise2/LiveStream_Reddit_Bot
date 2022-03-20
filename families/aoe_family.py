"""
This family file was auto-generated by generate_family_file.py script.

Configuration parameters:
  url = https://liquipedia.net/ageofempires
  name = aoe

Please do not commit this to the Git repository!
"""
from pywikibot import family


class Family(family.Family):  # noqa: D101

    name = 'aoe'
    langs = {
        'en': 'liquipedia.net',
    }

    def scriptpath(self, code):
        return {
            'en': '/ageofempires',
        }[code]

    def protocol(self, code):
        return {
            'en': 'https',
        }[code]
