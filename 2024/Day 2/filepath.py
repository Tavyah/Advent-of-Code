import os

def get_current_filepath() -> str:
    return os.path.dirname(os.path.realpath(__file__))