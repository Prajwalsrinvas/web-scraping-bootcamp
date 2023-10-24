import scrapy

from countries_gdp.items import CountryGdpItem


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

            item = CountryGdpItem()
            ## xpath selector
            item["country_name"] = country.xpath("td[1]/a/text()").get()
            item["region"] = country.xpath("td[2]/a/text()").get()
            item["gdp"] = country.xpath("td[3]/text()").get()
            item["year"] = country.xpath("td[4]/text()").get()
            yield item
