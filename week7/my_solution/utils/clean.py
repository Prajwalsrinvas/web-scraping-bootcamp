import os
from datetime import datetime

import pandas as pd


def clean_mrp(mrp):
    return float(mrp.strip("₹").replace(",", ""))


def clean_price(price):
    return float(price.strip("₹").replace(",", ""))


def clean_discount(discount):
    return int(discount.strip("-%"))


def clean_thumbnail(thumbnail):
    return thumbnail.split("?")[0]


def clean_reviews_count(reviews_count):
    return int(reviews_count.strip("| ").replace(" User Reviews", "").replace(",", ""))


def clean(parsed_data):
    df = pd.DataFrame(parsed_data)
    df["mrp"] = df["mrp"].apply(clean_mrp)
    df["price"] = df["price"].apply(clean_price)
    df["discount"] = df["discount"].apply(clean_discount)
    df["reviews_count"] = df["reviews_count"].apply(clean_reviews_count)
    df["thumbnail"] = df["thumbnail"].apply(clean_thumbnail)
    print("[x] Cleaned data")
    return df


def save_data(data):
    os.makedirs("data", exist_ok=True)
    file_name = f"steam_offers_{datetime.now():%Y_%m_%d_%H_%M_%S}.csv"
    file_path = os.path.join("data", file_name)
    print(f"[x] Data saved: {file_path}")
    data.to_csv(file_path, index=False)


def print_data(data):
    # remove tags and thumbnail as they take a lot of space while printing
    del data["tags"]
    del data["thumbnail"]
    print(
        data.sort_values("discount", ascending=False).to_markdown(
            index=False, tablefmt="rounded_grid"
        )
    )
