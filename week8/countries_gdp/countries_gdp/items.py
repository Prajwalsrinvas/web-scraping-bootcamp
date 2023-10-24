# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_commas(value):
    return value.replace(",", "")


def convert_int(value):
    try:
        return int(value)
    except ValueError:
        return value


def extract_year(value):
    year = re.findall(r"\d{4}", value)
    if not year:
        return value
    return year


class CountryGdpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country_name = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst()
    )
    region = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst()
    )
    gdp = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, remove_commas, convert_int),
        output_processor=TakeFirst(),
    )
    year = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, extract_year, convert_int),
        output_processor=TakeFirst(),
    )
