from typing import List, Optional
import requests
import re


def find_news() -> Optional[List]:
    """
    in this function we go to https://lenta.ru and find there news's links
    :return: Optional[List]
    """
    data = requests.request('GET', 'https://lenta.ru/').text
    links = re.findall(r'"/news/\S*"', data)
    ready_links = ['https://lenta.ru/' + str(link[1:-2]) for link in links]
    return ready_links
