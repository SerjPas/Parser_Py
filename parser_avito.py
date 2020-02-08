import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    """
    Create new object soup from libery BeautifulSoup
    :param html and type of document we work with 'html.parser'

    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='na-card-item')

    print(items)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        # call the object
        get_content(html.text)
    else:
        print("Error")


parse()
