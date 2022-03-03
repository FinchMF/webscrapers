import argparse
from crawlers.baudrillard import BaudrillardCrawler
from crawlers.politician import PoliticianCrawler


class Scrapers():

    def scrapeBaudrillard(self):

        crawler = BaudrillardCrawler(verbose=True)

        texts = [
            'simulations',
            'simulacra-and-simulations'
        ]

        [ crawler.craw(title=title) for title in texts ]


    def scrapePoliticians(self) -> None:

        crawler = PoliticianCrawler(verbose=True)
        crawler.fetchSpeeches()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '-identity', type=str, help='name of author')

    args = parser.parse_args()

    if args.i == 'baudrillard':
        Scrapers().scrapeBaudrillard()

    elif args.i == 'politicians':
        Scrapers().scrapePoliticians()

    else:
        raise Exception('please choose between: baudrillard or politicians')