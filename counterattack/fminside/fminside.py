"""A module for scraping fminside.com for club or player information.

functions:
    fetch_club_fm_data: Scrapes club information on a club's page from fminside.com
    fetch_player_fm_data: Scrapes player information on a player's page from fminside.com

exceptions:
    This module doesn't currently use any try-except blocks.
"""

import requests
from bs4 import BeautifulSoup as bs
from lxml import etree


def fetch_club_fm_data(url):
    """Scrapes club information from a club's page at fminside.com

    Args:
        url (str): the URL to a club's page at fminside.com

    Returns:
        club_name (str): the name of the club.
        fm_version (str): the version of Football Mananger this data comes from.
        player_urls (list): a list containing the URLs to each of the club's players' individual pages on fminside.com
    """
    r = requests.get(url).text
    soup = bs(r, 'html.parser')
    dom = etree.HTML(str(soup))
    club_name = soup.find('h1').get_text()
    fm_version = str(dom.xpath('//*[@id="club"]/div/div[1]/ul/li[1]/span[2]/text()')[0]).replace(" ", "")
    search = soup.find_all("div", class_='players') # search for divs containing lists of players (this likely returns more than 1 list)
    longest_list = None
    z = 0
    for i in search: # 'search' results give 4 list items which are 4 different tables of players. We want the longest one for the "Full Squad"
        if len(i) > z:
            z = len(i)
            longest_list = i
    full_squad = [i for i in longest_list.contents if len(i) > 5] # dropping any list item with length <= 5
    players_urls = [full_squad[x].find("span", class_='name').a['href'] for x in range(0,len(full_squad))] # get the url for each player and put in list form
    return club_name, fm_version, players_urls

def fetch_player_fm_data(url):
    """Scrapes player information from a player's page at fminside.com

    Args:
        url (str): the URL to a player's page at fminside.com

    Returns:
        name (str): the name of the player.
        nation (str): the nationality of the player.
        skills (dict): a dictionary containining all of the Football Manager stats for the player.
        fm_version (str): the version of Football Mananger this data comes from.

    Constant Variables:
        NATION_CONV (dict): a dictionary containing (key) Football Mananger country names and (value) Counter Attack country names used to convert from FM to CA.
    """
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    dom = etree.HTML(str(soup))
    name = str(dom.xpath('//*[@id="player"]/div[2]/ul/li[1]/span[2]/text()')[0])
    fm_version = str(dom.xpath('//*[@id="main_body"]/ul/li[1]/a/text()')[0]).replace(" ", "")
    NATION_CONV = {
        # Football Mananger: Counter Attack
        'Republic of Ireland': 'Ireland',
        'United States': 'Usa',
        'Czech Republic': 'Czechia',
        'Bosnia and Herzegovina': 'Bosnia',
        'Dominican Republic': 'Dominicana',
        'Central African Republic': 'Central Africa',
        'Democratic Republic of Congo': 'DR Congo'
    }
    nation_result = dom.xpath('//*[@id="player"]/div[1]/div/ul/li[2]/span/a/text()')
    nation = nation_result[0]
    if nation in NATION_CONV.keys():
        nation = NATION_CONV[nation]
    else:
        nation = nation
    skills = {}
    skills_result = soup.find("div", id='player_stats').find_all('tr')
    for i in skills_result:
        skill = i['id']
        value = i.td.next_sibling.next_sibling.string
        skills[skill] = int(value)
    return name, nation, skills, fm_version

