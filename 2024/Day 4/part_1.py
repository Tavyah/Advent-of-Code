import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *
import filepath as fp

def main() -> None:
    URL = 'https://adventofcode.com/2024/day/4/input'
    INPUT_FILE = 'input_data.txt'
    #content = scrape_input_site(URL)
    #make_txt_file(content, INPUT_FILE, fp.get_current_filepath())

    text = reading_txt_data('sample_data.txt', fp.get_current_filepath())
    crossword_puzzle = []
    for i in text:
        crossword_puzzle.append(i.split())

    print(crossword_puzzle)

if __name__ == "__main__":
    main()