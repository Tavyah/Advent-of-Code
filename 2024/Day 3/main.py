import sys, os
import filepath as fp
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *

URL = 'https://adventofcode.com/2024/day/3/input'
INPUT_FILENAME = 'input_data.txt'

#website_content = scrape_input_site(URL)
#make_txt_file(website_content, INPUT_FILENAME, fp.get_current_filepath())

text = reading_txt_data(INPUT_FILENAME, fp.get_current_filepath())
regex_string = 'mul\(\d+,\d+\)'
matches = re.findall(regex_string, text)

total = 0
for i in matches:
    i = i.strip('mul(')
    i = i.strip(')')
    number_1, number_2 = i.split(',')
    total += int(number_1) * int(number_2)

print(total)
make_txt_file(str(total), 'answer_part_1.txt', fp.get_current_filepath())