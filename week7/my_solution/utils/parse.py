import json

from selectolax.lexbor import LexborHTMLParser


def get_value(element, type):
    if type == "text":
        value = element[0].text()
    elif type == "img":
        value = element[0].attributes["src"]
    elif type == "text_list":
        value = [i.text() for i in element]
    return value


with open("utils/parser_config.json") as f:
    parser_config = json.load(f)


def parse(data):
    tree = LexborHTMLParser(data)
    page = tree.css_first("div.facetedbrowse_FacetedBrowseItems_NO-IP")

    lst = []
    games = page.css("div.salepreviewwidgets_SaleItemBrowserRow_y9MSd")
    for game in games:
        data = {}
        for field in parser_config:
            if field["required"]:
                data[field["field"]] = get_value(
                    game.css(field["selector"]), field["type"]
                )
        lst.append(data)

    print("[x] Parsed data")
    return lst
