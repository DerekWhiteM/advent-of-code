def getIndexOfMaxValue(stringArray):
    max = int(stringArray[0])
    maxIndex = 0
    for i in range(len(stringArray)):
        value = int(stringArray[i])
        if value > max:
            max = value
            maxIndex = i
    return maxIndex

def getMaxJoltage(bank):
    index1 = getIndexOfMaxValue(bank[:len(bank)-1])
    value1 = bank[index1]
    index2 = getIndexOfMaxValue(bank[index1+1:])
    value2 = bank[index1+index2+1]
    return int(f"{value1}{value2}") 

sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        bank = list(line)
        sum += getMaxJoltage(bank)

print(sum)
