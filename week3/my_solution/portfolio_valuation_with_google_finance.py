import json

import pandas as pd
import requests
from bs4 import BeautifulSoup

# user input
with open("stocks.json") as f:
    stocks = json.load(f)


def convert_currency(price, input_currency, output_currency):
    if input_currency == output_currency:
        return price
    url = f"https://www.google.com/finance/quote/{input_currency}-{output_currency}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    conversion_rate = float(
        soup.find("div", attrs={"data-entity-type": "3"})["data-last-price"]
    )
    converted_price = price * conversion_rate
    return round(converted_price, 2)


def get_price(ticker, exchange, output_currency):
    print(f"Crawling {ticker}:{exchange}")
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    stock_info = soup.find("div", attrs={"data-entity-type": "0"})
    input_currency = stock_info["data-currency-code"]
    price = float(stock_info["data-last-price"])
    converted_price = convert_currency(price, input_currency, output_currency)
    print(f"{input_currency} {price} ==> {output_currency} {converted_price}\n")
    return converted_price


output_currency = stocks["output_currency"]
total_portfolio_value = 0
for stock in stocks["stocks"]:
    price = get_price(stock["ticker"], stock["exchange"], output_currency)
    market_value = price * stock["quantity"]
    stock.update({"price": price, "market_value": market_value})
    total_portfolio_value += market_value
total_portfolio_value = total_portfolio_value


# add percent_allocation
for stock in stocks["stocks"]:
    percent_allocation = (stock["market_value"] / total_portfolio_value) * 100
    stock.update({"percent_allocation": round(percent_allocation, 2)})


print(pd.DataFrame(stocks["stocks"]).to_markdown(index=False, tablefmt="rounded_grid"))


print(f"Total portfolio value: {output_currency} {total_portfolio_value}")
