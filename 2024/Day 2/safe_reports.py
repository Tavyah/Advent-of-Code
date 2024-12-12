import requests as r
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *

def main() -> None:
    url = 'https://adventofcode.com/2024/day/2/input'
    body_of_website = scrape_input_site(url)
    print(body_of_website)
                                                                                                              
if __name__ == "__main__":
    main()