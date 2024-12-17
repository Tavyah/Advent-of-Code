import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *
import filepath as fp

def main() -> None:
    INPUT_FILENAME = 'input_data.txt'
    disk = reading_txt_data('sample_data.txt', fp.get_current_filepath())
    disk = generate_file_compacting_process(disk)
    
    find_checksum(disk)

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
    #print(file_compact_list)
    lookup_table = generate_lookup_table_for_dots(file_compact_list)

    while(not done_with_moving_blocks):
        
        last_queued_files = find_all_same_file_sizes(file_compact_list)
        print(last_queued_files)
        if '.' in file_compact_list:
            string_to_replace = file_compact_list.index('.')
            #file_compact_list[string_to_replace] = last_file
            file_compact_list.pop(-1)
        else:
            done_with_moving_blocks = True

    return file_compact_list

def generate_file_compacting_process(disk : str) -> list:
    file_compact_string = generate_file_compacting_string(disk)
    return move_file_blocks(file_compact_string)

def find_checksum(compact_process : list) -> None:
    checksum = 0
    
    for i in range(0, len(compact_process)):
        checksum += (int(compact_process[i]) * i)

    print(checksum)
    make_txt_file(str(checksum), 'answer_part_2.txt', fp.get_current_filepath())

def generate_lookup_table_for_dots(disk: list) -> dict:
    lookup_table = {}
    amount_of_free_space = 0
    for i in range(0, len(disk)):
        if disk[i] == '.':
            amount_of_free_space += 1
            if disk[i+1] != '.':
                lookup_table[i-(amount_of_free_space-1)] = amount_of_free_space
                amount_of_free_space = 0

    return lookup_table

def find_all_same_file_sizes(disk: list) -> dict:
    last_file = disk[-1]
    amount_of_space = 0
    for i in reversed(range(0, len(disk))):
        if disk[i] == last_file:
            amount_of_space += 1
            print(disk[i])
            print(disk[i-1])
            if disk[i-1] != last_file:
                break
    return {last_file : amount_of_space}

if __name__ == "__main__":
    main()