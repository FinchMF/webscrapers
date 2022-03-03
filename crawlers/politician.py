import os
import re
import requests
from bs4 import BeautifulSoup

from crawlers import LOG

class Paths:

    pages: int = 100000
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

        for link in speech_links:

            url: str = f"{Paths.root}{link}"
            title: str = url.split('/')[-1]

            try:

                res: object = requests.get(url)
                
            except Exception as err:
                LOG.info(err)
                continue

            page: object = BeautifulSoup(res.content, 'html.parser')

            text: list = [ i.get_text() for i in page.find_all('p') ]

            pres_name: str = '-'.join(''.join(text[1:2]).replace('.', '').split(' ')).lower()
            dos: str = '-'.join(''.join(text[2:3]).replace('.', '').split(' ')).lower()

            if self.verbose: LOG.info(f'Speech on Date: {dos} given by {pres_name}')

            try:
                os.mkdir(f'{PoliticianCrawler.textRoot}{pres_name}')
                if self.verbose: LOG.info(f'Directory Made: {pres_name}')

            except FileExistsError:
                _file: str = f'{PoliticianCrawler.textRoot}{pres_name}/{title}.txt'
                with open(_file, 'w') as f:
                    for t in text[3:-2]:
                        f.write(f'{t}\n')

    def fetchSpeeches(self) -> None:

        regex: str = '/the-presidency/presidential-speeches/'
        speech_links: list = []

        for page in range(0, Paths.pages):

            if self.verbose: LOG.info(f'Page {page} Gathered.....')

            try:
                speeches: str = f'{Paths.speeches_page}{Paths.page_url}{page}'

                res: object = requests.get(speeches)
                page: object = BeautifulSoup(res.content, 'html.parser')

                links: list  = [ link['href'] for link in page.find_all('a', href=True) if re.match(regex, link['href']) ]

                if len(links) == 0:
                    LOG.info(f'Reached End of Pages...')
                    break
                speech_links.extend(links)

            except Exception as err:
                LOG.info(err)
                

        self.saveSpeeches(speech_links=speech_links)