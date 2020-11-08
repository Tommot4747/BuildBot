from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint as pp

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


pp(mobi_champ_links())