import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_writers(soup, id):
    try:
        actorLines = soup.find('span', {'itemprop':'creator', 'itemprop': 'name'}).text
        return actorLines
    except:
        print('Couldnt parse writers for id ' + id)
        return None