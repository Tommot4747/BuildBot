import requests
from bs4 import BeautifulSoup

# "Constants" to help decide url
MOBAFIRE = "https://mobafire.com" # will probably add more
# can add relevant filterable aspects here such updated or descending etc.
LANE = "" #probably not
RUNESPATH1 = "" # ex tree + 1/2/3 + spells + tree + 1/2 + bonuses
SUM_SPELLS = ""
RUNESPATH2 = ""
ITEMSPATH = ""
ABILITIESPATH = ""

'''
https://www.mobafire.com/league-of-legends/browse?champion=(character name here) 
 (this is the minimum needed for a search)

https://www.mobafire.com/league-of-legends/browse?champion=Zed
&role=all
&category=all
&depth=guide
&sort=updated
&order=descending
&author=all&
page=1
'''

'''
Research of .html of target page
guide titles use the H3 header
<h3 class="browse-list__item__desc__title ajax-tooltip { t:'Build',i:'573303' }">RoninDraco&#039;s 1M ZED One Trick Season 10 Guide</h3>

'''


source = requests.get(MOBAFIRE).text

soup = BeautifulSoup(source, 'lxml')
# page --> wrapper --> content --> col-left --> 
# browse-list(has links) --> 
# ---- content above has links to each guide ----
# --> browse-list__item__desc
# --> browse-list__item__desc__tags
# --> li.text???? or classname.text (current-patch-shine)
# ---- content should have the patch information ----
# --> div browse-list__item__rating
# --> div browse-list__item__rating__total
# ---- content above has the rating of the post, identified as total. Can also use views ----

'''
"
											
						current-patch patch-shinetooltip
				"'''

# for rows in "col-left"


print(soup.prettify())