# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryGdpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country_name = scrapy.Field()
    region = scrapy.Field()
    gdp = scrapy.Field()
    year = scrapy.Field()
