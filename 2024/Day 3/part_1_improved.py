import sys, os
import filepath as fp
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *

def main() -> None:
    URL = 'https://adventofcode.com/2024/day/3/input'
    INPUT_FILENAME = 'input_data.txt'

    #website_content = scrape_input_site(URL)
    #make_txt_file(website_content, INPUT_FILENAME, fp.get_current_filepath())

    text = reading_txt_data(INPUT_FILENAME, fp.get_current_filepath())
    stripped_list = strip_data(text)
    count_mul_sum(stripped_list)
    #make_txt_file(str(total), 'answer_part_2.txt', fp.get_current_filepath())

def count_mul_sum(data: list) -> None:
    total = 0

    for numbers in data:
        total += multiply_two_numbers(numbers)
    
    print(total)

def multiply_two_numbers(numbers: list) -> int:
    number = [numbers[i] * numbers[i-1] for i in range(1, len(numbers))]
    return number[0]

def strip_data(text: str) -> list:
    muls = re.findall('mul\(\d+,\d+\)', text)
    numbers = [list(map(int, re.findall('\d+', mul))) for mul in muls]
    return numbers

if __name__ == "__main__":
    main()