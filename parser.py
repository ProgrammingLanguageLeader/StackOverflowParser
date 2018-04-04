from argparse import ArgumentParser
from bs4 import BeautifulSoup
from requests import request


if __name__ == '__main__':
    url = 'https://stackoverflow.com'
    search_url = 'https://stackoverflow.com/search'

    parser = ArgumentParser()
    parser.add_argument(
        'question',
        help='a string that contains your question'
    )
    args = parser.parse_args()
    question = args.question

    reply = request(
        method='get',
        url=search_url,
        params={
            'q': question
        }
    )
    soup = BeautifulSoup(reply.text, 'html.parser')
    search_results = soup.select(
        'div.search-result div.summary div.result-link a'
    )
    for search_result in search_results:
        print('%s%s' % (url, search_result.attrs['href']))
