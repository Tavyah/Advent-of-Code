import configparser
import filehandler_helper as fh
import requests as r

def get_config_username_and_password(section_name: str, username_label: str, password_label: str) -> tuple[str, str]:
    config = configparser.ConfigParser()
    config_filename = 'config.ini'
    filepath = fh.return_filepath_joined_with_file(fh.get_current_filepath(), config_filename)
    config.read(filepath)
    db_username = config.get(section_name, username_label)
    db_password = config.get(section_name, password_label)
    return db_username, db_password

def make_cookie() -> dict:
    name, value = get_config_username_and_password('cookie', 'name', 'value')
    my_cookie = {
        name: value
    }
    return my_cookie

def scrape_input_site(url: str) -> str:
    cookies = make_cookie()
    response = r.get(url, cookies= cookies)
    return response.text

def make_txt_file(content: str, name_of_file: str, filepath: str) -> None:
    fp = fh.return_filepath_joined_with_file(filepath, name_of_file)
    with open(fp, "w") as file:
        file.write(content) 

def reading_txt_data(filename: str, filepath: str) -> str:
    file_to_read = fh.get_path_of_file(filepath, filename)

    file = open(file_to_read, "r", encoding='cp1252')
    file_content = file.read()
    file.close()
    return file_content