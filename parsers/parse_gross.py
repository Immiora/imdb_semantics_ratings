import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_gross(soup, id):
    try:
        for h4 in soup.find_all('h4'):
            if "Gross:" in h4:
                gross = h4.next_sibling.strip()
                return gross

        return None
    
    except:
        print('Could not parse gross for id ' + id)
        return None