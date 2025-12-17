def getMaxJoltage(bank):
    joltageArray = bank[:12]
    for i in range(12, len(bank)):
        for j in range(12):
            if (j == 12-1):
                if (bank[i] > joltageArray[j]):
                    joltageArray.pop(j)
                    joltageArray.append(bank[i])
            elif (joltageArray[j+1] > joltageArray[j]):
                joltageArray.pop(j)
                joltageArray.append(bank[i])
                break
    return int("".join(joltageArray))

total = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        bank = list(line)
        joltage = getMaxJoltage(bank)
        total += joltage 

print(sum)
