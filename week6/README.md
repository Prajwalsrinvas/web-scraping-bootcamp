# Quotes Scraper [`(JS rendered version)`](http://quotes.toscrape.com/js/) 

## Week 6 goal:

- Catch up on Week 4 and Week 5 pending content (if any).
- Practice CSS selectors by completing all levels of [CSS diner](https://flukeout.github.io/).
- Tackling JavaScript With Microsoft PlayWright.
---

## 📍Overview

The project is a collection of scripts that use various web scraping libraries to extract quotes and their authors from web pages. The purpose of the project is to showcase different web scraping techniques and to provide examples of how to extract specific information from HTML content.

---

## Quotes scraped using 3 methods:

- Requests-HTML:
    - HTML Parsing for Humans (writing Python 3)!
    - https://requests.readthedocs.io/projects/requests-html/en/latest/
    - https://github.com/psf/requests-html
- Splash:
    - A javascript rendering service.
    - https://splash.readthedocs.io/en/stable/index.html
    - https://github.com/scrapinghub/splash
- Playwright:
    - enables reliable end-to-end testing for modern web apps.
    - https://playwright.dev/python/docs/intro
    - https://github.com/microsoft/playwright-python

## 💻 Modules

Sure! Here's the table without the Module column:

| File                            | Summary                                                                                                                                                                                                                                                                                                                         |
|:--------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| quotes_scraper_splash.py        | The code imports necessary libraries, pulls HTML content using Splash from a given URL, extracts specific information using CSS selectors and compiles the resulting data into a dictionary. The extracted info in this case pertains to quotes and their respective authors.                                                   |
| quotes_scraper_requests_html.py | This code uses the requests_html library to scrape quotes and their authors from a webpage. It renders the webpage, extracts the relevant text using specified selectors, and converts the data into a dictionary format. The function is then called when the script is run.                                                   |
| quotes_scraper_playwright.py    | The code snippet uses Playwright to automate web scraping of quotes and their authors from a website. It then converts the scraped data into a dictionary format using the quotes_list_to_dict function. The code launches Chromium, navigates to the specified URL, extracts data using CSS selectors, and closes the browser. |
| utils.py                        | This code imports the `json` library and defines the URL and selectors for a web scraping project. The `quotes_list_to_dict` function takes two lists of quotes and authors and converts them into a dictionary format. It then writes the resulting data into a `quotes.json` file using the `json.dump` function.                 |



