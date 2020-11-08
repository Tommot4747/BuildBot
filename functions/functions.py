import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

def stat_table(champ_json, champ_id):
    stats_json = champ_json['data'][champ_id]['stats']

    stats_stagnant = ["armor", "attackdamage", "attackrange", "attackspeed", "crit",
    "hp", "hpregen", "movespeed", "mp", "mpregen", "spellblock"]

    champ_stats = []
    stats_headers = ['Stat', '1','2','3','4','5','6','7','8','9','10','11','12','13',                       '14','15','16','17','18']
    champ_stats.append(stats_headers)
    
    
    for stat in stats_stagnant:
        stat_amount = stats_json[stat]
        stat_list = [stat, str(stat_amount)]
        try:
            stat_addition = stats_json[stat + 'perlevel']
            for i in range(1, 18):
                level_rank = stat_amount + (stat_addition * i)
                stat_list.append(str(round(level_rank,2)))
        except:
            for i in range(1, 18):
                stat_list.append(str(round(stat_amount,2)))
        champ_stats.append(stat_list)


    df = pd.DataFrame(columns=champ_stats[0], data=champ_stats[1:])
    return champ_stats, df

def mobi_champ_links():
    url = 'https://www.mobafire.com'
    html_doc = requests.get(f'{url}').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    footer_div = soup.find('div', class_ = 'footer-links')
    footer_tags = footer_div.find_all('a', href=True)
    champ_links = {}
    for champ in footer_tags:
        champ_key = champ.text
        champ_value = url + champ['href']
        champ_links[champ_key] = champ_value
    return champ_links



def mobi_build_lookup(champ_link):
    html_doc = requests.get(f'{champ_link}?sort=patch&order=ascending&author=all&page=1').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    a_tags = soup.find_all('a', class_ = re.compile('browse-list'))
    full_link = 'https://www.mobafire.com' + a_tags[0]['href']
    return full_link