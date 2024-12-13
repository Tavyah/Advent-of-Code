import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *

def main() -> None:
    url = 'https://adventofcode.com/2024/day/2/input'
    input_filename = 'input_data.txt'
    filepath = get_current_filepath()

    #body_of_website = scrape_input_site(url)
    #make_txt_file(body_of_website, input_filename, filepath()) 

    content_of_file = reading_txt_data(input_filename, filepath)
    safe_reports = calculate_safe_reports(content_of_file)

    make_txt_file(str(safe_reports), 'answer_part_2.txt', get_current_filepath())

def get_current_filepath() -> str:
    return os.path.dirname(os.path.realpath(__file__))

def calculate_safe_reports(data_to_analyze: str) -> int:
    safe = 0
    first = True
    prev_number = 0
    lines_analyzed = 0
    amount_of_sorted_lists = 0
    amount_of_unique_lists = 0
    qualified_list = 0

    for i in data_to_analyze:
        lines_analyzed += 1
        list = i.strip('\n').split(' ')
        parsed_list = [int(number) for number in list]

        last_index = len(parsed_list) - 1
        current_index = -1
        #print(parsed_list)

        sorted_list = is_list_sorted(parsed_list)
        unique_list = is_list_unique(parsed_list)
        print(f"parsed: {parsed_list}")
        if sorted_list:
            amount_of_sorted_lists += 1
            #parsed_list, safe, first = remove_element_that_is_not_needed(parsed_list, last_index, current_index, safe, first)
        else:
            
            if unique_list:
                # Her ska æ sjekke alle de usorterte listene om de e sortert fra et visst element
                for element in range(0, len(parsed_list)):
                    if rest_of_list_is_sorted(element, parsed_list):
                        parsed_list.pop(element)
                        break
                sorted_list = True
                
            else:
                duplicate_location = find_location_of_duplicates(parsed_list)
    
                if duplicate_location is not None:
                    parsed_list.pop(duplicate_location)
                    unique_list = True
                    
        if unique_list:
            amount_of_unique_lists += 1
        print(f"etter: {parsed_list}")
        print(f"qualified: {unique_list} {sorted_list}")
        if sorted_list and unique_list:  
            qualified_list += 1
            safe, first = check_list_for_differance(parsed_list, last_index, current_index, prev_number, safe, first)

        first = True
        
    print(f"Number of lines analyzed: {lines_analyzed}/1000.")
    print(f"There are a total of {lines_analyzed - amount_of_sorted_lists} unsorted lists.")
    print(f"And there is {amount_of_unique_lists} of unique lists in the data.")
    print(f"Of the {qualified_list} qualified lists only {safe} are actually safe reports.")
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

def find_location_of_duplicates(parsed_list: list) -> int:
    first = True
    prev_number = 0

    for i in range(0, len(parsed_list)):
        if first:
            prev_number = parsed_list[i]
            first = False
            continue
        if prev_number == parsed_list[i]:
            return i
        
def rest_of_list_is_sorted(element : int, parsed_list : list) -> bool:
    temp_list = parsed_list[:]
    temp_list.pop(element)
    return is_list_sorted(temp_list)

def remove_element_that_is_not_needed(parsed_list: list, last_index: int, current_index: int, safe: int, first: bool) -> list | int | bool:
    
    
    return parsed_list, safe, first

def check_list_for_differance(parsed_list: list, last_index: int, current_index: int, prev_number: int, safe: int, first: bool) -> int | bool:
    for number in parsed_list:
                current_index += 1

                if first:
                    first = False
                    prev_number = number
                    continue
                
                diff = calculate_diff(number, prev_number)
                
                if diff > 3 or diff < 1:
                    parsed_list.pop(current_index)
                else:
                    if last_index == current_index:
                        safe += 1
                    prev_number = number
    return safe, first

if __name__ == "__main__":
    main()