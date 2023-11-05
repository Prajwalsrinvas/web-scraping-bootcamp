import scrapy
from scrapy import Request
from scrapy_playwright.page import PageMethod


class HfJobsSpiderSpider(scrapy.Spider):
    name = "hf_jobs_spider"
    allowed_domains = ["workable.com"]

    def start_requests(self):
        url = "https://apply.workable.com/huggingface/?lng=en#jobs"
        yield Request(
            url,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod(
                        "wait_for_selector",
                        'ul[data-ui="list"]',
                    ),
                    PageMethod(
                        "evaluate",
                        """
                            const interval_id = setInterval(function () {
                            const next_button = document.querySelector('button[data-ui="load-more-button"]');
                            if (next_button) {
                                next_button.scrollIntoView();
                                next_button.click();
                            }
                            else {
                                clearInterval(interval_id)
                            }
                        }, 1000)
                        """,
                    ),
                    PageMethod(
                        "wait_for_selector",
                        'button[data-ui="load-more-button"]',
                        state="detached",
                    ),
                ],
            },
        )

    async def parse(self, response):
        for i in response.css('ul[data-ui="list"] li'):
            data = {
                "title": i.css('h2[data-ui="job-title"] span::text').get(),
                "workplace": i.css('span[data-ui="job-workplace"]::text').get(),
                "location": i.css('span[data-ui="job-location"]::text').get(),
                "department": i.css('span[data-ui="job-department"]::text').get(),
                "type": i.css('span[data-ui="job-type"]::text').get(),
                "link": f"https://apply.workable.com{i.css('a::attr(href)').get()}",
            }
            yield data
