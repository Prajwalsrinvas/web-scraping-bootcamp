import scrapy
from periodic_table.items import PeriodicTableItem
from scrapy import Request
from scrapy.loader import ItemLoader
from scrapy_playwright.page import PageMethod


class PeriodicTableSpiderSpider(scrapy.Spider):
    name = "periodic_table_spider"
    allowed_domains = ["pubchem.ncbi.nlm.nih.gov"]

    def start_requests(self):
        url = "https://pubchem.ncbi.nlm.nih.gov/ptable/"
        yield Request(
            url,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod(
                        "wait_for_selector",
                        "#main-content > div > div.break-before-avoid.break-inside-avoid",
                    )
                ],
            },
        )

    async def parse(self, response):
        elements = response.css(
            '#main-content > div > div.break-before-avoid.break-inside-avoid  div.element[role="listitem"]'
        )
        for element in elements:
            item = ItemLoader(item=PeriodicTableItem(), selector=element)
            item.add_xpath("symbol", './/div[@data-tooltip="Symbol"]/text()')
            item.add_xpath("name", './/div[@data-tooltip="Name"]/text()')
            item.add_xpath(
                "atomic_number", './/div[@data-tooltip="Atomic Number"]/text()'
            )
            item.add_xpath(
                "atomic_mass", './/div[@data-tooltip="Atomic Mass, u"]/text()'
            )
            item.add_xpath(
                "chemical_group",
                './/div[@data-tooltip="Chemical Group Block"]/span/text()',
            )
            yield item.load_item()
