import filehandler_helper as fh
import re

def main() -> None:
    file_content = reading_txt_data()
    left_list, right_list = split_file_object_to_two_lists(file_content)
    left_list.sort()
    right_list.sort()
    distances = find_distance_between_two_numbers(left_list, right_list)
    print(calculate_total_distance(distances))

def reading_txt_data() -> str:
    filename = "locations_data.txt"
    filepath = fh.get_current_filepath()
    file_to_read = fh.get_path_of_file(filepath, filename)

    file = open(file_to_read, "r", encoding='cp1252')
    file_content = file.readlines()
    file.close()
    return file_content

def split_file_object_to_two_lists(file_content :str) -> list:
    left_list = []
    right_list = []

    for line in file_content:
        line = line.split('   ')

        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

    return left_list, right_list

def find_distance_between_two_numbers(left_list: list, right_list: list) -> list:
    list_with_distances = []
    
    for number in range(0, len(left_list)):
        distance = abs(left_list[number] - right_list[number])
        list_with_distances.append(distance)

    return list_with_distances

def calculate_total_distance(list: list) -> int:
    total = 0
    for number in list:
        total += number

    return total

if __name__ == "__main__":
    main()