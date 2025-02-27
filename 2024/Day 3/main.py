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

regex_string = "do\(\).*?don't\(\)"
matches = re.findall(regex_string, text)
#print(matches)

regex_last_match = "don't\(\).*?do\(\).*"
regex_last_matches = list(re.finditer(regex_last_match, text))
print(regex_last_matches[-1].group())
make_txt_file(regex_last_matches[-1].group(), 'last_match.txt', fp.get_current_filepath())
#print(last_match)

do_matches = []

regex_do_string = "do\(\).*?do\(\)"
for i in range(0, len(matches)):
    clean_matches = re.findall(regex_do_string, matches[i])
    if not clean_matches:
        do_matches.append(matches[i])
    else:
        for j in clean_matches:
            do_matches.append(j)

total = 0

first_regex_mul = "mul\(\d+,\d+\).*?don't\(\)"
first_mul = re.search(first_regex_mul, text)
do_matches.append(first_mul.group())

regex_strip = 'mul\(\d+,\d+\)'

for i in range(0, len(do_matches)):
    match = re.findall(regex_strip, do_matches[i])

    for each_match in match:
        each_match = each_match.strip('mul(')
        each_match = each_match.strip(')')
        number_1, number_2 = each_match.split(',')

        total += int(number_1) * int(number_2)


print(total)
make_txt_file(str(total), 'answer_part_2.txt', fp.get_current_filepath())
