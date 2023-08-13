# Steam Game Offers Scraper

This Python project is designed to extract information about the highest discounted games from the Steam store. It includes several files that work together to achieve this task.

## Project Structure

The project contains the following files:

### main.py

This is the main entry point of the project. It orchestrates the different steps of the scraping process:

1. It gets the configuration from `tools.get_config()`.
2. It extracts the full HTML body from a specified URL using `utils.extract.extract_full_body_html()`.
3. It parses raw attributes from the extracted HTML using `utils.parse.parse_raw_attributes()`.
4. It processes and formats the parsed data using `utils.process.format_and_transform()`.
5. It saves the extracted game data to a file using `utils.process.save_to_file()`.

### tools.py

This file contains the project configuration, which can be loaded from a JSON file or generated programmatically. It includes settings such as the target URL, selectors for different elements on the page, and metadata about the scraper.

### extract.py

This file is responsible for extracting the full HTML body from a given URL using the Playwright library. It utilizes a headless Chromium browser to load the page, wait for necessary elements, and retrieve the HTML content.

### parse.py

This file contains the logic to parse raw attributes from a given HTML node or string using CSS selectors. It can extract text or nodes based on the specified selectors and return the parsed data as a dictionary.

### process.py

This file contains data processing functions. It includes functions to reformat dates, apply regular expressions, and transform extracted attributes into a consistent format. The main function here is `format_and_transform()`, which applies various transformations to the extracted attributes.

## Usage

To use this project:

1. Run `main.py` to initiate the scraping process.
2. Modify the configuration in `tools.py` to adjust the scraping behavior.
3. Ensure the required Python packages (Playwright, pandas, selectolax) are installed.

## Configuration

The configuration in `tools.py` defines the following settings:

- `url`: The target URL for scraping (default: "https://store.steampowered.com/specials").
- `container`: CSS selectors for the main container that holds the game sale previews.
- `item`: CSS selectors for individual game sale items, including attributes like title, thumbnail, tags, release date, review score, prices, etc.

The configuration can be loaded from a JSON file or generated programmatically using the provided functions.

## Output

The extracted game data is saved as a CSV file with a filename containing the current date and the name "extract". The data includes attributes such as game title, thumbnail URL, tags, release date, review score, prices, and more.

## Dependencies

This project relies on the following Python packages:

- Playwright (for web scraping)
- pandas (for data processing)
- selectolax (for HTML parsing)

Make sure these packages are installed in your environment before running the project.
