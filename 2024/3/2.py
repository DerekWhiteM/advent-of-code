import re

pattern = r'(?:mul\(\d+,\d+\))|(?:do\(\))|(?:don\'t\(\))'
contents = None

with open('input.txt', 'r') as file:
    contents = file.read()


matches = re.findall(pattern, contents)
result = 0
do = True

for match in matches:
    if match == 'do()' or match == "don't()":
        do = match == 'do()'
        continue
    if do:
        sub_pattern = r'\d+,\d+'
        sub_matches = re.findall(sub_pattern, match)
        values = sub_matches[0].split(',')
        result += (int(values[0]) * int(values[1]))

print(result)