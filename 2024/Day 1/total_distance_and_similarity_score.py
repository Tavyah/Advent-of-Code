import filehandler_helper as fh

def main() -> None:
    file_content = reading_txt_data()
    left_list, right_list = split_file_object_to_two_lists(file_content)
    left_list.sort()
    right_list.sort()
    distances = find_distance_between_two_numbers(left_list, right_list)
    print(calculate_total_distance(distances))
    print(similarity_score(left_list, right_list))

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

    answer_filename = 'answer_part_1.txt'
    filepath = fh.get_current_filepath()
    filename = fh.return_filepath_joined_with_file(filepath, answer_filename)
    with open(filename, 'w') as file:
        file.write(str(total))

    return total

def similarity_score(left_list: list, right_list: list) -> int:
    occurences_in_right_list = return_unique_dict_with_occurences(right_list)
    occurences_in_left_list = return_unique_dict_with_occurences(left_list)
    unique_left_list = return_unique_list(left_list)
    similarity_score = 0
    for number in unique_left_list:
        try:
            similarity_score += ((number * occurences_in_left_list[number]) * occurences_in_right_list[number])
        except KeyError:
            continue

    answer_filename = 'answer_part_2.txt'
    filepath = fh.get_current_filepath()
    filename = fh.return_filepath_joined_with_file(filepath, answer_filename)
    with open(filename, 'w') as file:
        file.write(str(similarity_score))
    return similarity_score
    
def return_unique_dict_with_occurences(list: list) -> dict:
    # Parsing the list so I find the unique values
    list_unique_values = return_unique_list(list)

    dict_with_how_many_unique_values_in_list = {}
    for unique_value in list_unique_values:
        dict_with_how_many_unique_values_in_list[unique_value] = list.count(unique_value)
    
    return dict_with_how_many_unique_values_in_list

def return_unique_list(list: list) -> set:
    return set(list)

if __name__ == "__main__":
    main()