"""
helper module to fetch state of the union 2022, joe biden
"""
import requests
from bs4 import BeautifulSoup


def retrieve_speech_text(url: str) -> str:

    res = requests.get(url)
    page = BeautifulSoup(res.content, 'html.parser')
    text = ''.join([ i.get_text() for i in page.find_all('p') ])

    return text
    

def writeOut(text: str, fname: str) -> dict:

    res = {}

    try:

        with open(fname, 'w') as f:
            f.write(text)
        
        res['success'] = True

    except Exception as err:

        res['sucess'] = False
        res['error'] = err

    return res


def run(url: str, fname: str) -> None:

    text = retrieve_speech_text(url=url)
    res = writeOut(text=text, fname=fname)

    if res['success']:
        return
    else:
        print(res['error'])


if __name__ == '__main__':

    URL = 'https://www.whitehouse.gov/state-of-the-union-2022/'
    fname = 'state-of-the-union-2022.txt'

    run(url=URL, fname=fname)
    print('Done')