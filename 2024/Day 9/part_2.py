import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *
import filepath as fp

def main() -> None:
    INPUT_FILENAME = 'input_data.txt'
    disk = reading_txt_data(INPUT_FILENAME, fp.get_current_filepath())
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
    number_of_files = set(file_compact_list)
    moved = False
    blacklist = []

    slice_indices = generate_file_indices(file_compact_list)

    for i in reversed(range(0, len(number_of_files)-1)):
        print(f"{i}/{len(number_of_files)-1}")

        slice_index = slice_indices[i]
        lookup_table = generate_lookup_table_for_dots(file_compact_list, slice_index)
        last_queued_files = find_all_same_file_sizes(file_compact_list, blacklist)
        
        try:
            if not isinstance(last_queued_files[i], int):
                continue
        except KeyError:
            continue
        
        for j in lookup_table:
            if lookup_table[j] >= last_queued_files[i]:
                # Move block
                moved = True
                for k in range(j, j+last_queued_files[i]):
                    file_compact_list[k] = i
                break
        if moved:    
            slice_list = file_compact_list[slice_index:slice_index + last_queued_files[i]]
            for number in range(0,len(slice_list)):
                if slice_list[number] == i:
                    slice_list[number] = '.'
            file_compact_list[slice_index:slice_index + last_queued_files[i]] = slice_list
            blacklist.append(i)
        else:
            blacklist.append(i)
        moved = False

    return file_compact_list

def generate_file_compacting_process(disk : str) -> list:
    file_compact_string = generate_file_compacting_string(disk)
    return move_file_blocks(file_compact_string)

def find_checksum(compact_process : list) -> None:
    checksum = 0
    
    for i in range(0, len(compact_process)):
        if isinstance(compact_process[i], int):
            checksum += (int(compact_process[i]) * i)

    print(checksum)
    make_txt_file(str(checksum), 'answer_part_2.txt', fp.get_current_filepath())

# This function is ridiciliously long and consuming alot of computer power
def generate_lookup_table_for_dots(disk: list, position : int) -> dict:
    lookup_table = {}
    amount_of_free_space = 0
    for i in range(0, len(disk)):
        if i == position:
            break
        if disk[i] == '.':
            amount_of_free_space += 1
            try:
                if disk[i+1] != '.':
                    lookup_table[i-(amount_of_free_space-1)] = amount_of_free_space
                    amount_of_free_space = 0
            except IndexError:
                lookup_table[i-(amount_of_free_space-1)] = amount_of_free_space
                amount_of_free_space = 0

    return lookup_table

def find_all_same_file_sizes(disk: list, blacklist : list) -> dict:
    index = 1

    for i in range(index, len(disk)):
        if isinstance(disk[-index], int) and disk[-index] not in blacklist:
            last_file = disk[-index]
            break
        else:
            index += 1

    amount_of_space = 0
    for i in reversed(range(0, len(disk))):
        if disk[i] == last_file:
            amount_of_space += 1
            if disk[i-1] != last_file:
                break
    return {last_file : amount_of_space}

def generate_file_indices(file_compact_list: list) -> dict:
    file_indices = {}
    unique_indices = set(file_compact_list)
    for i in range(0, len(unique_indices)-1):
        file_indices[i] = file_compact_list.index(i)
    print(unique_indices)
    return file_indices
if __name__ == "__main__":
    main()