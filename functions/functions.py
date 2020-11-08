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
    first_link = 'https://www.mobafire.com' + a_tags[0]['href']
    second_link = 'https://www.mobafire.com' + a_tags[1]['href']
    third_link = 'https://www.mobafire.com' + a_tags[2]['href']
    return first_link, second_link, third_link

def counter_champ_links():
    url = 'https://www.counterstats.net'
    html_doc = requests.get(f'{url}').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    champion_div = soup.find('div', id = 'champions')
    champion_tags = champion_div.find_all('div', class_ = 'champion-icon champList')
    champ_links = {}
    for champ in champion_tags:
        champ_key = str(champ.text).replace('\n', '')
        counter_page = champ.find('a', href=True)
        champ_value = url + counter_page['href']
        champ_links[champ_key] = champ_value
    return champ_links

def counter_champ_lookup(champ_link):
    html_doc = requests.get(f'{champ_link}').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    all_picks_tags = soup.find_all('div', class_ = 'champ-box ALL')
    counterers_dict = {'best' : [], 'worst' : []}
    for box in all_picks_tags:
        if box.find('em', class_ = 'green') != None:
            counterers = box.find_all('a', class_ = re.compile('radial-progress'))
            for counter in counterers:
                counter_dict = {}

                img_ele = counter.find('img')
                img = img_ele['src']
                name = img_ele['alt'].split('for ')[-1].strip()
                percent = counter.find('span', class_ = 'percentage').text.strip()

                counter_dict['name'] = name
                counter_dict['img'] = img
                counter_dict['percent'] = percent

                counterers_dict['best'].append(counter_dict)

        elif box.find('em', class_ = 'red') != None:
            counterers = box.find_all('a', class_ = re.compile('radial-progress'))
            for counter in counterers:
                counter_dict = {}

                img_ele = counter.find('img')
                img = img_ele['src']
                name = img_ele['alt'].split('for ')[-1].strip()
                percent = counter.find('span', class_ = 'percentage').text.strip()

                counter_dict['name'] = name
                counter_dict['img'] = img
                counter_dict['percent'] = percent

                counterers_dict['worst'].append(counter_dict)
    return counterers_dict

def counter_message(champ_name, counter_champ_dict):
    best_list = counter_champ_dict['best']
    worst_list = counter_champ_dict['worst']
    
    message = f"*info from Counterstats.net*: \n**Best Against {champ_name}** \n **1.**{best_list[0]['name']} \
        {best_list[0]['percent']}\n **2.**{best_list[1]['name']} {best_list[1]['percent']}\n **3.**{best_list[2]['name']} \
        {best_list[2]['percent']}\n **Worst Against {champ_name}** \n **1.**{worst_list[0]['name']} {worst_list[0]['percent']}\n **2.**{worst_list[1]['name']} \
        {worst_list[1]['percent']}\n **3.**{worst_list[2]['name']} {worst_list[2]['percent']}"
    return message

def stats_message(champ_name, champ_id, champ_detail_json, win_stats_dict):
    ally = ', '.join(champ_detail_json['data'][champ_id]['allytips'])
    enemy = ', '.join(champ_detail_json['data'][champ_id]['enemytips'])
    
    message = f"You have locked in {champ_name} \n **Ally Tips**: {ally} \n **Enemy Tips**: {enemy} \n\
        **Win** {win_stats_dict['win']} \n **Ban** {win_stats_dict['ban']} \n **Pick** {win_stats_dict['pick']}"
    return message

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