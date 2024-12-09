import re

contents = None
with open('input.txt', 'r') as file:
    contents = file.read()

pattern = r'mul\(\d+,\d+\)'
matches = re.findall(pattern, contents)

result = 0

for match in matches:
    sub_pattern = r'\d+,\d+'
    sub_matches = re.findall(sub_pattern, match)
    values = sub_matches[0].split(',')
    result += (int(values[0]) * int(values[1]))

print(result)