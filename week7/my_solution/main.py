from utils.clean import clean, print_data, save_data
from utils.fetch import fetch_page
from utils.parse import parse

data = fetch_page()
parsed_data = parse(data)
clean_data = clean(parsed_data)
save_data(clean_data)
print_data(clean_data)
