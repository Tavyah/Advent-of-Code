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
    #make_txt_file(body_of_website, input_filename, filepath) 

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
    popped_element = False
    prev_number = 0
    lines_analyzed = 0
    amount_of_sorted_lists = 0
    amount_of_unique_lists = 0

    qualified_list = 0
    qualified_safe_list = 0

    not_unique_list = 0
    qualified_not_unique_list = 0

    not_sorted_list = 0
    qualified_not_sorted_list = 0
    j = 0
    k = 0
    
    parsed_list = _split_string_to_int_list(data_to_analyze)
    
    for i in parsed_list:
        lines_analyzed += 1
        current_index = -1

        sorted_list = is_list_sorted(i)
        unique_list = is_list_unique(i)

        if sorted_list:
                amount_of_sorted_lists += 1

        if unique_list:
                amount_of_unique_lists += 1

        if sorted_list and unique_list:
            # SORTED and UNIQUE
            print('start')
            qualified_list += 1
            last_index = set_last_index(i)
            temp_safe = safe
            safe, first, i, popped_element = check_list_for_differance(i, last_index, current_index, prev_number, safe, first, popped_element)
            if temp_safe < safe:
                 qualified_safe_list += 1
        else:
            if not unique_list:
                # NOT UNIQUE, can be SORTED or NOT SORTED
                print('duplikat')
                not_unique_list += 1
                i, unique_list = find_location_of_duplicates(i)
                popped_element = True
                sorted_list = is_list_sorted(i)
                last_index = set_last_index(i)

                if unique_list and sorted_list:
                    qualified_not_unique_list += 1
                    temp_safe = safe
                    safe, first, i, popped_element = check_list_for_differance(i, last_index, current_index, prev_number, safe, first, popped_element)
                    if temp_safe < safe:
                         j += 1
            else:
                # UNIQUE, can be SORTED or NOT SORTED
                print('can sort')
                not_sorted_list += 1
                last_index = set_last_index(i)
                # Check if can make NOT SORTED list -> SORTED
                i, popped_element = check_if_can_sort(i, last_index, current_index, prev_number, safe, first, popped_element)
                sorted_list = is_list_sorted(i)
                # Returns either SORTED or NOT SORTED

                last_index = set_last_index(i)
                
                if unique_list and sorted_list:
                    qualified_not_sorted_list += 1
                    temp_safe = safe
                    safe, first, i, popped_element = check_list_for_differance(i, last_index, current_index, prev_number, safe, first, popped_element)
                    if temp_safe < safe:
                         k += 1

        first = True
        popped_element = False
        sorted_list = False
        unique_list = False
        
    print(f"Number of lines analyzed: {lines_analyzed}/1000.")
    print(f"There are a total of {lines_analyzed - amount_of_sorted_lists} unsorted lists.")
    print(f"And there is {amount_of_unique_lists} of unique lists in the data.")
    print(f"Of the {qualified_list} qualified lists only {qualified_safe_list} are actually safe reports.")
    print(f"Of the {not_unique_list} not unique qualified lists only {j}/{qualified_not_unique_list} are actually safe reports.")
    print(f"Of the {not_sorted_list} not sorted qualified lists only {k}/{qualified_not_sorted_list} are actually safe reports.")
    print('\n===========================================================================================\n')
    print(f'                                Total safe reports: {safe}')
    print('\n===========================================================================================')
    
    return safe

def set_last_index(list: list) -> int:
     return len(list) - 1

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

def find_location_of_duplicates(list: list) -> list | bool:
    new_list = list[:]
    duplicate = [i for i in Counter(list) if Counter(list)[i] > 1]
    new_list.pop(list.index(duplicate[0]))
    if is_list_sorted(new_list):
         return new_list, is_list_unique(new_list)
    else:
         last_index = len(list) - 1 - list[::-1].index(duplicate[0])
         list.pop(last_index)
         return list, is_list_unique(list)
        
def rest_of_list_is_sorted(element : int, i : list) -> bool:
    temp_list = i[:]
    temp_list.pop(element)
    return is_list_sorted(temp_list)
# TODO finn ut av denne funksjonen
def check_list_for_differance(i: list, last_index: int, current_index: int, prev_number: int, safe: int, first: bool, popped_element: bool) -> int | bool | list | bool:
    while True:
        temp_list = i[:]
        current_index = -1
        first = True
        prev_number = 0

        for number in temp_list:
            current_index += 1

            if first:
                first = False
                prev_number = number
                continue
            
            diff = calculate_diff(number, prev_number)
            
            if diff > 3 or diff < 1:
                if not popped_element:
                    temp_list, popped_element = check_if_can_sort(temp_list, last_index, current_index, prev_number, safe, first, popped_element)
                    if popped_element:
                        i = temp_list
                        
                else:
                    break

            if last_index == current_index:
                safe += 1

            prev_number = number

        return safe, first, temp_list, popped_element

def check_if_can_sort(list: list, last_index: int, current_index: int, prev_number: int, safe: int, first: bool, popped_element: bool) -> list | bool:
    list_with_potentials = []
    # Her ska æ sjekke alle de usorterte listene om de e sortert fra et visst element
    for element in range(0, len(list)):
        if rest_of_list_is_sorted(element, list):
            list_with_potentials.append(element)
            
    if len(list_with_potentials) == 1:
        list.pop(list_with_potentials[0])
        popped_element = True
    else:
        list, popped_element = check_what_to_pop(list, list_with_potentials, last_index, current_index, prev_number, safe, first, popped_element)  

    return list, popped_element

def check_what_to_pop(list: list, list_with_potentials: list, last_index: int, current_index: int, prev_number: int, safe: int, first: bool, popped_element: bool) -> list | bool:
    
    temp_list = list[:]
    for i in list_with_potentials:
        temp_list.pop(i)
        popped_element = True
        last_index = set_last_index(temp_list)
        temp_safe = safe
        safe, first, new_list, popped_element = check_list_for_differance(temp_list, last_index, current_index, prev_number, safe, first, popped_element)   
        
        if temp_safe < safe and not popped_element:
            list.pop(i)
            popped_element = True
            break
        if temp_safe < safe:
             return temp_list, popped_element
        temp_list = list[:]
        first = True
    return list, popped_element


if __name__ == "__main__":
    main()