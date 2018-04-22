from argparse import ArgumentParser
from bs4 import BeautifulSoup

from requests import request


def fetch_question_page_links(question):
    search_url = 'https://stackoverflow.com/search'
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
    return search_results


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        'question',
        help='a string that contains your question'
    )
    args = arg_parser.parse_args()
    question = args.question

    question_pages = fetch_question_page_links(question)
    page_urls = [
        'https://stackoverflow.com/%s' % page.attrs['href']
        for page in question_pages
    ]
    for page_url in page_urls:
        print(page_url)
