import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *
import filepath as fp

def main() -> None:
    URL = 'https://adventofcode.com/2024/day/9/input'
    INPUT_FILE = 'input_data.txt'
    #content = scrape_input_site(URL)
    #make_txt_file(content, INPUT_FILE, fp.get_current_filepath())

    disk = reading_txt_data(INPUT_FILE, fp.get_current_filepath())
    file_compact_string = generate_file_compacting_process(disk)
    file_compact_list = move_file_blocks(file_compact_string)
    find_checksum(file_compact_list)
    
def generate_list_with_disk_info(disk: str) -> list:
    disk = disk.strip('\n')
    list_with_files = []

    for i in range(1, len(disk), 2):
        list_with_files.append([disk[i-1], disk[i]])
    list_with_files.append([disk[-1]])

    return list_with_files

def generate_file_compacting_string(disk: str) -> list:
    file_info = generate_list_with_disk_info(disk)
    compact_string = []
    for i in range(0, len(file_info)):
        for j in range(0, int(file_info[i][0])):
            compact_string.append(i)
        try:
            for k in range(0, int(file_info[i][1])):
                compact_string.append('.')
        except IndexError:
            continue
    return compact_string

def move_file_blocks(file_compact_list: list) -> list:
    done_with_moving_blocks = False

    while(not done_with_moving_blocks):
        last_file = file_compact_list[-1]
        if '.' in file_compact_list:
            string_to_replace = file_compact_list.index('.')
            file_compact_list[string_to_replace] = last_file
            file_compact_list.pop(-1)
        else:
            done_with_moving_blocks = True

    return file_compact_list

def generate_file_compacting_process(disk : str) -> str:
    file_compact_string = generate_file_compacting_string(disk)
    return move_file_blocks(file_compact_string)

def find_checksum(compact_process : list) -> None:
    checksum = 0
    
    for i in range(0, len(compact_process)):
        checksum += (int(compact_process[i]) * i)

    print(checksum)
    make_txt_file(str(checksum), 'answer_part_1.txt', fp.get_current_filepath())

if __name__ == "__main__":
    main()