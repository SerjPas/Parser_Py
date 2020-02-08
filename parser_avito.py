import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        pass
    else:
        print("Error")


parse()
