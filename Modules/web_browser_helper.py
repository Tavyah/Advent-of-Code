import configparser
import filehandler_helper as fh
import requests

def get_config_username_and_password(section_name: str, username_label: str, password_label: str) -> tuple[str, str]:
    config = configparser.ConfigParser()
    config_filename = 'config.ini'
    filepath = fh.return_filepath_joined_with_file(fh.get_current_filepath(), config_filename)
    config.read(filepath)
    db_username = config.get(section_name, username_label)
    db_password = config.get(section_name, password_label)
    return db_username, db_password

def make_cookie(url: str) -> requests:
    s = requests.Session()
    username, password = get_config_username_and_password('github', 'user', 'pass')
    s.auth = (username, password)
    return s.cookies.set("session", "53616c7465645f5f82c736dfc95f2427f503eafd80fa765c85b63910806af61baa5de38a70c168fb09516f3ac5017612a6bb5155a02af231f8b7668262d7935e", domain=url)