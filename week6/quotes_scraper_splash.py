import requests
from selectolax.lexbor import LexborHTMLParser

from utils import URL, author_selector, quote_selector, quotes_list_to_dict

"""
docker pull scrapinghub/splash
docker run -it -p 8050:8050 --rm scrapinghub/splash
"""


def get_quotes():
    splash_url = "http://localhost:8050/render.html"
    splash_options = {
        "url": URL,
    }

    response = requests.get(splash_url, params=splash_options)
    tree = LexborHTMLParser(response.text)

    quotes_list = [i.text() for i in tree.css(quote_selector)]
    authors_list = [i.text() for i in tree.css(author_selector)]
    quotes_list_to_dict(quotes_list, authors_list)


if __name__ == "__main__":
    get_quotes()
