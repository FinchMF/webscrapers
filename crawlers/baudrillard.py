import requests
from bs4 import BeautifulSoup

from crawlers import LOG

class ScraperError(Exception):
    pass


class Paths:

    archiveRoot: str = 'https://archive.org/stream/'
    simulations: str = f'{archiveRoot}Simulations1983/Baudrillard_Simulations_djvu.txt'
    simulationAndSimulacra: str = f'{archiveRoot}simulacra-and-simulation-1995-university-of-michigan-press/Simulacra_and_Simulation_1995_University_of_Michigan_Press__djvu.txt'


class BaudrillardCrawler(object):

    textRoot: str = "./data/baudrillard/"

    def __init__(self, verbose: bool = False):

        self.__text: dict = {}
        self.__verbose: bool = verbose 

    @property
    def text(self) -> dict:
        return self.__text

    @property
    def verbose(self) -> dict:
        return self.__verbose

    def chooseText(self, title: str) -> None:

        self.title: str = title

        if title == 'simulations':
            endpoint: str = Paths.simulations
            
        elif title == 'simulacra-and-simulations':
            endpoint: str = Paths.simulationAndSimulacra

        else:
            raise ScraperError(f'Title: {title} not supported.\
            Please choose from: "simulations" | "simulacra-and-simulations"')

        self.endpoint: str = endpoint

        if self.verbose:
            LOG.info(f'Scrapping Endpoint: {self.endpoint}')

    def scrapeText(self) -> None:

        res: object = requests.get(self.endpoint)
        page: object = BeautifulSoup(res.content, 'html.parser')

        self.text[self.title]: str = page.find(id='maincontent').find('pre').text

        if self.verbose:
            LOG.info(f'{self.title} scrapped..')

    def saveText(self) -> None:

        _file: str = f'{BaudrillardCrawler.textRoot}{self.title}.txt'

        with open(_file, 'w') as f:
            f.write(self.text[self.title])

        if self.verbose:
            LOG.info(f'Saved at: {_file}')

    def crawl(self, title: str, save: bool = True) -> None:

        self.chooseText(title=title)
        self.scrapeText()
        if save: self.saveText()

