# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


class PeriodicTableItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    symbol = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    atomic_number = scrapy.Field(
        input_processor=MapCompose(int), output_processor=TakeFirst()
    )
    atomic_mass = scrapy.Field(
        input_processor=MapCompose(float), output_processor=TakeFirst()
    )
    chemical_group = scrapy.Field(output_processor=TakeFirst())
