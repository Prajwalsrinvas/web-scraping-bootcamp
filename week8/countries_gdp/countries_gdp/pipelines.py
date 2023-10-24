# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CountriesGdpPipeline:
    def process_item(self, item, spider):
        if not isinstance(item["gdp"], int):
            raise DropItem("Item excluded as gdp is missing")
        return item


class NoDuplicateCountryPipeline:
    def __init__(self):
        self.countries_seen = set()

    def process_item(self, item, spider):
        if item["country_name"] in self.countries_seen:
            raise DropItem(f"Item excluded as country is duplicate: {item}")
        else:
            self.countries_seen.add(item["country_name"])
            return item


class SaveToDatabasePipeline:
    def __init__(self):
        self.con = sqlite3.connect("countries_gdp.db")
        self.cur = self.con.cursor()

    def open_spider(self, spider):
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS countries_gdp 
        (country_name TEXT PRIMARY KEY,
        region TEXT,
        gdp INTEGER,
        year INTEGER) 
        """
        )
        self.con.commit()

    def process_item(self, item, spider):
        self.con.execute(
            """
        INSERT INTO countries_gdp (country_name, region, gdp, year) VALUES (?, ?, ?, ?)        
        """,
            (item["country_name"], item["region"], item["gdp"], item["year"]),
        )
        self.con.commit()

    def close_spider(self, spider):
        self.con.close()
