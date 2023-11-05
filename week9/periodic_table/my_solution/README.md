# Dynamic Periodic Table Scraper 🧪

## Introduction
- **Objective**: Extract, process, and structure data from the PubChem website's Periodic Table.
- **Technology**: Utilizes the Scrapy-PlayWright framework for web scraping and data processing.
- **Data Elements**: Extracts information about chemical elements, including symbol, name, atomic number, atomic mass, and chemical group.
- **Structured Storage**: Stores the extracted data in a structured manner for further analysis or applications.

## Usage
- Clone the repo
- Install requirements
```bash
pip install -r requirements.txt
```
- Start the scraping process by running the Scrapy spider:
```bash
scrapy crawl periodic_table_spider
```

- The scraped data will be stored in the SQLite database (periodic_table.db) and a JSON file (chemical_groups.json).

### Components

#### `periodic_table/items.py`
This module defines the data structure for scraped items. It specifies the fields for each chemical element, such as symbol, name, atomic number, atomic mass, and chemical group.

#### `periodic_table/settings.py`
The Scrapy settings file. It configures various aspects of the Scrapy framework, such as bot name, spider modules, item pipelines, download handlers, and more. You can adjust these settings to suit your project's requirements.

#### `periodic_table/pipelines.py`

- `GroupByChemicalGroupPipeline`: This pipeline groups the scraped elements by their chemical group and counts the number of elements in each group. The results are stored in a JSON file named `chemical_groups.json`.

- `SaveToDatabasePipeline`: This pipeline saves the scraped data to an SQLite database named `periodic_table.db`. It creates a table for the periodic table and inserts the data into it.

#### `periodic_table/spiders/periodic_table_spider.py`
This Scrapy spider defines the web scraping process. It starts by making a request to the PubChem website, scrapes information about chemical elements, and uses Item Loaders to populate the defined fields in `periodic_table/items.py`. The data is then passed through the pipelines defined in `periodic_table/pipelines.py`.
