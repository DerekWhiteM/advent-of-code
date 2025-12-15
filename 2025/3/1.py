def getMaxValue(stringArray):
    max = stringArray[0]
    for string in stringArray:
        value = int(string)
        if value > max:
            max = value



'''
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        bank = list(line)
        print(bank)
'''

