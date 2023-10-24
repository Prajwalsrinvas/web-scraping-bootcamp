# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


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
        input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst()
    )
