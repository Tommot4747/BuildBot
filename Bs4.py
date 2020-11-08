from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint as pp

import requests
from bs4 import BeautifulSoup

url = 'https://www.mobafire.com/league-of-legends/build/yeagers-master-zed-guide-532930'

def mobi_assets(mobi_link):
    html_doc = requests.get(f'{mobi_link}').text
    soup = BeautifulSoup(html_doc, 'html.parser')

    primary = soup.find('div', class_ = 'new-runes__primary')
    primary_runes = []

    #primary runes - note first image is branch
    for runes in primary.find_all('div', class_ = 'new-runes__item'):
        image = runes.find('img')['src']
        primary_runes.append(image) # note it still needs mobafire.com in front

    secondary = soup.find('div', class_ = 'new-runes__secondary')
    secondary_runes = []

    #secondary runes - note first image is branch
    for runes in secondary.find_all('div', class_ = 'new-runes__item'):
        image = runes.find('img')['src']
        secondary_runes.append(image)

    bonus = soup.find('div', class_ = 'new-runes__bonuses')
    bonus_attr = []

    #bonus attributes
    for attrs in bonus.find_all('img'):
        image = attrs['src']
        bonus_attr.append(image)

    summoners = soup.find('div', class_ = 'view-guide__spells')
    summoner_spells = []
    # summoner spells
    for spells in summoners.find_all('div', class_ = 'view-guide__spells__row'):
        image = spells.find('img')['src']
        summoner_spells.append(image)

    summoners = soup.find('div', class_ = 'view-guide__spells')
    summoner_spells = []

    print(primary_runes)
    print(secondary_runes)
    print(bonus_attr)
    print(summoner_spells)




pp(mobi_assets(url))
# counter_champ_links()