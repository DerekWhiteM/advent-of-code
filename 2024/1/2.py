'''
Calculate the total similarity score of the lists. 
Similarity score = number * frequency
'''

# Create a map of numbers and their frequencies from list 2
frequency_map = {}
numbers = set()

# Compute frequency map
with open('input.txt', 'r') as file:
    for line in file:
        columns = line.split()
        number1 = int(columns[0])
        number2 = int(columns[1])
        numbers.add(number1)
        if number2 in frequency_map:
            frequency_map[number2] += 1
        else:
            frequency_map[number2] = 1

sum = 0

len = len(numbers)

for i in range(len):
    key = numbers.pop()
    sum += (key * frequency_map.get(key, 0))

print(sum)