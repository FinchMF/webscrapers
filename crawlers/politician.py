import requests
from bs4 import BeautifulSoup

from crawlers import LOG

class Paths:

    pages: int = 150
    root: str = 'https://millercenter.org'
    speeches_page: str = 'https://millercenter.org/the-presidency/presidential-speeches'
    page_url: str = '?field_speech_date_value%5Bmin%5D=&field_speech_date_value%5Bmax%5D=&field_full_node_value=&page='


class PoliticianCrawler(object):

    textRoot: str = "./data/politicians/"

    def __init__(self, verbose: bool = False):

        self.__verbose: bool = verbose

    @property
    def verbose(self) -> bool:
        return self.__verbose

    def saveSpeeches(self, speech_links: str) -> None:

        pass

    def fetchSpeeches(self) -> None:

        pass

    
