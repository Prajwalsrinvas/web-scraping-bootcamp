import json

URL = "http://quotes.toscrape.com/js/"
quotes_blocks_selector = "div.quote"
quote_selector = "span.text"
author_selector = "small.author"


def quotes_list_to_dict(quotes_list, authors_list):
    quotes = []
    for quote, author in zip(quotes_list, authors_list):
        quotes.append({"quote": quote.strip("“”"), "author": author})
    with open("quotes.json", "w") as f:
        json.dump(quotes, f, indent=4)
