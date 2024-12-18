import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *
import filepath as fp

def main() -> None:
    URL = 'https://adventofcode.com/2024/day/10/input'
    INPUT_FILE = 'input_data.txt'
    #make_txt_file(scrape_input_site(URL),INPUT_FILE,fp.get_current_filepath())
    data = reading_txt_data('sample_data.txt', fp.get_current_filepath())
    print(find_total_paths(data))

def _split_data_list(data: list ) -> list:
    data = data.split()
    new_data = []
    for each in data:
        new_data.append(list(each))
    new_data = [list(map(int, inner_list)) for inner_list in new_data]
    return new_data

def find_total_paths(data: list) -> int:
    total_paths = 0
    next_list = 0
    data = _split_data_list(data)
    
    while True:
        try:
            for i in range(0, len(data[next_list])):

                if data[next_list][i] == 0:
                    number_of_paths = check_for_path(data, [next_list, i])
                    total_paths += number_of_paths
            next_list += 1
        except IndexError:
            break
            
    return total_paths
# TODO
def check_for_path(data : list, current_position_in_list : list) -> int:
    number_of_paths_found = 0
    next_number = 1
    last_number = 9
    current_list = current_position_in_list[0]
    current_position = current_position_in_list[1]

    print(current_position_in_list)
    for i in range(next_number, last_number):
        if i == data[current_list][current_position]:
            check_for_path(data, data[current_list][current_position])


    return number_of_paths_found

if __name__ == "__main__":
    main()