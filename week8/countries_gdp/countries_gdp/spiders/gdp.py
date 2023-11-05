import scrapy
from countries_gdp.items import CountryGdpItem
from scrapy.loader import ItemLoader


class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        ## css selector
        # countries = response.css("table.wikitable.sortable tbody tr:not([class])")

        ## xpath selector
        countries = response.xpath(
            "//table[contains(@class, 'wikitable') and contains(@class, 'sortable')]//tbody//tr[not(@class)]"
        )

        for country in countries:
            ## css selector

            # data = {
            #     "country_name": country.css("td:nth-child(1) a::text").get(),
            #     "region": country.css("td:nth-child(2) a::text").get(),
            #     "gdp": country.css("td:nth-child(3)::text").get(),
            #     "year": country.css("td:nth-child(4)::text").get(),
            # }

            item = ItemLoader(item=CountryGdpItem(), selector=country)
            ## xpath selector
            item.add_xpath("country_name", "td[1]/a")
            item.add_xpath("region", "td[2]/a")
            item.add_xpath("gdp", "td[3]")
            item.add_xpath("year", "td[4]")
            yield item.load_item()
