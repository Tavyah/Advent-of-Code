import requests as r
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *

def main() -> None:
    url = 'https://adventofcode.com/2024/day/2/input'
    input_filename = 'input_data.txt'
    filepath = get_current_filepath()

    body_of_website = scrape_input_site(url)
    #make_txt_file(body_of_website, input_filename, filepath()) 

    content_of_file = reading_txt_data(input_filename, filepath)
    print(calculate_safe_reports(content_of_file))

def get_current_filepath() -> str:
    return os.path.dirname(os.path.realpath(__file__))

def calculate_safe_reports(data_to_analyze: str) -> int:
    safe = 0
    first = True
    prev_number = 0

    for i in data_to_analyze:
        list = i.strip('\n').split(' ')
        parsed_list = [int(number) for number in list]  
        sorted_list = is_list_sorted(parsed_list)
        unique_list = is_list_unique(parsed_list)

        if sorted_list and unique_list:  
            for number in parsed_list:
                if first:
                    first = False
                    prev_number = number
                    continue
                diff = calculate_diff(number, prev_number)
                print(diff)
                if diff > 3 or diff < 1:
                    break
                else:
                    prev_number = number
            
    
    return safe

def calculate_diff(number1 : int, number2: int) -> int:
    return abs(number1 - number2)

def is_list_sorted(list: list) -> bool:
    if list == sorted(list):
        return True
    elif list == sorted(list, reverse= True):
        return True
    else:
        return False   

def is_list_unique(list: list) -> bool:
    return len(list) == len(set(list))

if __name__ == "__main__":
    main()