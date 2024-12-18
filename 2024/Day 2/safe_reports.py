import sys, os
from collections import Counter

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

def _split_string_to_int_list(string: str) -> list:
    new_list = []
    splitted_list = string.split('\n')
    for each in splitted_list:
        new_list.append(list(map(int, each.split())))
    return new_list

def calculate_safe_reports(data_to_analyze: str) -> int:
    safe = 0
    first = True
    prev_number = 0
    lines_analyzed = 0
    amount_of_sorted_lists = 0
    amount_of_unique_lists = 0
    qualified_list = 0
    popped_element = False
    
    parsed_list = _split_string_to_int_list(data_to_analyze)
    
    for i in parsed_list:
        print(i)
        lines_analyzed += 1
        last_index = len(i) - 1
        current_index = -1

        sorted_list = is_list_sorted(i)
        unique_list = is_list_unique(i)

        if sorted_list:
                amount_of_sorted_lists += 1

        if unique_list:
                amount_of_unique_lists += 1

        print(f"parsed: {i}")
        if sorted_list and unique_list:
            print('start')
            qualified_list += 1
            safe, first, i, popped_element = check_list_for_differance(i, last_index, current_index, prev_number, safe, first, popped_element)
        else:
            if not unique_list and not popped_element:
                print('duplikat')
                # TODO når æ finner duplikater så kan den poppe feil duplikat, må teste begge duplikater
                i = find_location_of_duplicates(i)
                safe, first, i, popped_element = check_list_for_differance(i, last_index, current_index, prev_number, safe, first, popped_element)
                popped_element = True
            elif not sorted_list and not popped_element:
                print('can sort')
                i = check_if_can_sort(i)
                safe, first, i, popped_element = check_list_for_differance(i, last_index, current_index, prev_number, safe, first, popped_element)
            else:
                print('else')

            
            print(f"etter: {i}")
            print(f"qualified: {unique_list} {sorted_list}")

        first = True
        popped_element = False
        
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

def find_location_of_duplicates(list: list) -> list:
    new_list = list[:]
    duplicate = [i for i in Counter(list) if Counter(list)[i] > 1]
    new_list.pop(list.index(duplicate[0]))
    if is_list_sorted(new_list):
         return new_list
    else:
         last_index = len(list) - 1 - list[::-1].index(duplicate[0])
         list.pop(last_index)
         return list
        
def rest_of_list_is_sorted(element : int, i : list) -> bool:
    temp_list = i[:]
    temp_list.pop(element)
    return is_list_sorted(temp_list)
# TODO finn ut av denne funksjonen
def check_list_for_differance(i: list, last_index: int, current_index: int, prev_number: int, safe: int, first: bool, popped_elemet: bool) -> int | bool | list | bool:
    for number in i:
                current_index += 1

                if first:
                    first = False
                    prev_number = number
                    continue
                
                diff = calculate_diff(number, prev_number)
                
                if diff > 3 or diff < 1:
                    if popped_elemet:
                        break
                    else:
                         i.pop(current_index)
                else:
                    if last_index == current_index:
                        safe += 1
                        popped_elemet = True
                    prev_number = number
    return safe, first, i, popped_elemet

def check_if_can_sort(list: list) -> list:
    # Her ska æ sjekke alle de usorterte listene om de e sortert fra et visst element
    for element in range(0, len(list)):
        if rest_of_list_is_sorted(element, list):
            list.pop(element)
            break
    return list

if __name__ == "__main__":
    main()