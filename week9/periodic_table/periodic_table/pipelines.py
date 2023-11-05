# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import sqlite3

from itemadapter import ItemAdapter


class PeriodicTablePipeline:
    def process_item(self, item, spider):
        return item


class GroupByChemicalGroupPipeline:
    def __init__(self):
        self.chemical_groups = {}

    def process_item(self, item, spider):
        chemical_group = item["chemical_group"]
        if chemical_group not in self.chemical_groups:
            self.chemical_groups[chemical_group] = {"element_count": 0, "elements": []}
        self.chemical_groups[chemical_group]["element_count"] += 1
        self.chemical_groups[chemical_group]["elements"].append(
            {k: v for k, v in item.items() if k != "chemical_group"}
        )

        return item

    def close_spider(self, spider):
        with open("chemical_groups.json", "w") as f:
            json.dump(self.chemical_groups, f)


class SaveToDatabasePipeline:
    def __init__(self):
        self.con = sqlite3.connect("periodic_table.db")
        self.cur = self.con.cursor()

    def open_spider(self, spider):
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS periodic_table 
        (symbol TEXT PRIMARY KEY,
        name TEXT,
        atomic_number INTEGER,
        atomic_mass REAL,
        chemical_group TEXT) 
        """
        )
        self.con.commit()

    def process_item(self, item, spider):
        self.con.execute(
            """
        INSERT INTO periodic_table (symbol, name, atomic_number, atomic_mass, chemical_group) VALUES (?, ?, ?, ?, ?)        
        """,
            (
                item["symbol"],
                item["name"],
                item["atomic_number"],
                item["atomic_mass"],
                item["chemical_group"],
            ),
        )
        self.con.commit()

    def close_spider(self, spider):
        self.con.close()
