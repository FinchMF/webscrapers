from crawlers.baudrillard import BaudrillardCrawler

def scrapeBaudrillard():

    crawler = BaudrillardCrawler(verbose=True)

    texts = [
        'simulations',
        'simulacra-and-simulations'
    ]

    for title in texts:
        crawler.crawl(title=title)


if __name__ == '__main__':

    scrapeBaudrillard()