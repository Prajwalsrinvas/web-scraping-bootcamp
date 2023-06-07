from requests_html import HTMLSession

from utils import URL, author_selector, quote_selector, quotes_list_to_dict


def get_quotes():
    session = HTMLSession()
    resp = session.get(URL)

    resp.html.render()

    quotes_list = [i.text for i in resp.html.find(quote_selector)]
    authors_list = [i.text for i in resp.html.find(author_selector)]
    quotes_list_to_dict(quotes_list, authors_list)


if __name__ == "__main__":
    get_quotes()
