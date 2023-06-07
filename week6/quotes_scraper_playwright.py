from playwright.sync_api import sync_playwright

from utils import URL, author_selector, quote_selector, quotes_list_to_dict


def get_quotes():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)

        quotes_list = [i.inner_text() for i in page.query_selector_all(quote_selector)]
        authors_list = [
            i.inner_text() for i in page.query_selector_all(author_selector)
        ]
        quotes_list_to_dict(quotes_list, authors_list)

        browser.close()


if __name__ == "__main__":
    get_quotes()
