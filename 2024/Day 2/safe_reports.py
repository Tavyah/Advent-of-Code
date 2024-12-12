import requests as r

respone = r.get('https://adventofcode.com/2024/day/2/input')
print(respone.text)