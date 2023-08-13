# Steam Game Offers Scraper

This Python project is a web scraper designed to fetch and clean data from the Steam Store's special offers page. It provides a convenient way to extract game-related information, including prices, discounts, reviews, and more. The project is divided into several components, each serving a specific purpose.

![output](assets/output.png)

## Project Structure

### main.py

This is the main script that orchestrates the entire process. It imports functions from various utility modules and executes them in the following order:

1. **fetch_page**: Fetches the Steam Store's special offers page using the Playwright library.
2. **parse**: Parses the fetched HTML content to extract relevant game data.
3. **clean**: Cleans the parsed data, transforming it into a structured pandas DataFrame.
4. **save_data**: Saves the cleaned data to a CSV file.
5. **print_data**: Prints a sorted and formatted version of the cleaned data, excluding certain columns for concise output.

### fetch.py

This module handles fetching the HTML content of the Steam Store's special offers page. It uses the Playwright library to perform the following steps:

1. Launch a headless Chromium browser.
2. Open the specified URL.
3. Scroll to the bottom of the page to ensure all data is loaded.
4. Wait for the page to reach a network idle state.
5. Extract the page content and close the browser.

### clean.py

The clean module is responsible for cleaning the raw game data extracted from the Steam Store's special offers page. It performs the following data cleaning operations:

1. Cleaning monetary values (mrp and price) to convert them to floats.
2. Cleaning discounts to convert them to integers.
3. Cleaning thumbnail URLs to remove unnecessary query parameters.
4. Cleaning reviews count to convert it to integers.
5. Saving the cleaned data to a CSV file with a timestamp.

### parse.py

The parse module handles the parsing of the HTML content to extract specific game-related information based on a configuration specified in the parser_config.json file. It performs the following steps:

1. Parse the HTML content using the LexborHTMLParser library.
2. Define a JSON-based configuration (parser_config) for extracting relevant fields from the parsed HTML.
3. Extract game data from the parsed HTML using the configured selectors and field types.

## Usage

To run the scraper and extract Steam game offers data, simply execute the main.py script. The script will fetch, parse, clean, and save the data to a CSV file, providing a formatted output for easy review.

Make sure you have the required libraries installed, such as Playwright, pandas, and LexborHTMLParser. Also, ensure that the parser_config.json file is properly configured to match the structure of the Steam Store's special offers page.

Feel free to customize this project for your specific use case or integrate it into larger data analysis pipelines.

**Note:** This project is intended for educational and non-commercial use only, and it's essential to respect Steam's terms of service and policies while scraping data from their website.
