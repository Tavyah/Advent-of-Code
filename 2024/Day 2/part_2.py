import sys, os
import filepath as fp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))

from web_browser_helper import *
from filehandler_helper import *

def main() -> None:
    input = 'input_data.txt'
    data = parse_content(reading_txt_data(input, fp.get_current_filepath()))
    count_safe_reports(data)

def count_safe_reports(reports: list) -> None:
    count = 0
    for report in reports:
        if is_safe_with_dampner(report):
            count += 1
    print(f'Total safe reports: {count}')

def is_safe_with_dampner(report: list) -> bool:
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    
    return False  

def is_safe(report: list) -> bool:
    is_increasing = all(report[i] >= report[i-1] for i in range(1, len(report)))
    is_decreasing = all(report[i] <= report[i-1] for i in range(1, len(report)))
    differences = [abs(report[i] - report[i-1]) for i in range(1, len(report))]
    valid_level_difference = all(1 <= diff <= 3 for diff in differences)

    return (is_increasing and valid_level_difference) or (is_decreasing and valid_level_difference)

def parse_content(content: str) -> list:
    return [list(map(int, line.split())) for line in content.strip().split('\n')]

if __name__ == "__main__":
    main()