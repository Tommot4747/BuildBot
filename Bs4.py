from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint as pp

link = 'https://www.mobafire.com/league-of-legends/zac-guide'

def mobi_stats_lookup(champ_link):
    html_doc = requests.get(f'{champ_link}').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    rates = soup.find_all('div', class_ = re.compile('winbanpick__item'))
    stats_dict = {}
    for rate in rates:
        if rate.find('span', class_ = 'label').text == 'WinRate':
            stats_dict['win'] = rate.find('span', class_ = 'perc').text
        elif rate.find('span', class_ = 'label').text == 'BanRate':
            stats_dict['ban'] = rate.find('span', class_ = 'perc').text
        elif rate.find('span', class_ = 'label').text == 'PickRate':
            stats_dict['pick'] = rate.find('span', class_ = 'perc').text
    return stats_dict



pp(mobi_stats_lookup(link))
# counter_champ_links()