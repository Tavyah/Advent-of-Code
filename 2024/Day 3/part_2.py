import sys, os
import filepath as fp
import re
from itertools import chain

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *

def main() -> None:
    URL = 'https://adventofcode.com/2024/day/3/input'
    INPUT_FILENAME = 'input_data.txt'

    #website_content = scrape_input_site(URL)
    #make_txt_file(website_content, INPUT_FILENAME, fp.get_current_filepath())

    text = reading_txt_data(INPUT_FILENAME, fp.get_current_filepath())
    stripped_list= strip_data(text)
    dont = dont_mul(text)
    do_or_dont = re.split(r"(do\(\)|don't\(\))", text)
    count_mul_sum(stripped_list, do_or_dont)
    
    #make_txt_file(str(total), 'answer_part_2.txt', fp.get_current_filepath())

def count_mul_sum(data: list, do_or_dont: list) -> None:
    total = 0

    for numbers in data:
        if do(do_or_dont, numbers):
            total += multiply_two_numbers(numbers)
    
    total += multiply_two_numbers(data[-1])
    print(total)

def do(mul : list, numbers: list) -> bool:
    #TODO fikse sånn at man veit ka sopm e ka
    if numbers in dont_mul:
        return False
    else:
        return True

def multiply_two_numbers(numbers: list) -> int:
    number = [numbers[i] * numbers[i-1] for i in range(1, len(numbers))]
    return number[0]

"""def dont_mul(text: str) -> list:
    numbers = []
    dont_muls = re.findall("don't\(\).*?mul\(\d+,\d+\).*?do\(\)", text)
    dont_muls = [list(map(str, re.findall('mul\(\d+,\d+\)', mul))) for mul in dont_muls]
    for muls in dont_muls:
        numbers.append([list(map(int, re.findall('\d+', mul))) for mul in muls])
    flat_numbers = list(chain.from_iterable(numbers))
    return flat_numbers"""

def strip_data(text: str) -> list | list:
    muls = re.findall('mul\(\d+,\d+\)', text)
    numbers = [list(map(int, re.findall('\d+', mul))) for mul in muls]
    return numbers

if __name__ == "__main__":
    main()