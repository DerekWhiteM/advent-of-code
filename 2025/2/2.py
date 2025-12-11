def isInvalid(num):
    string = str(num)
    strLen = len(string)
    midpoint = strLen // 2
    for i in range(1, midpoint + 1):
        partitions = partitionString(string, i)
        firstPart = partitions[0]
        allEqual = True
        for part in partitions:
            if part != firstPart:
                allEqual = False
                break
        if allEqual:
            return True
    return False

def partitionString(string, length):
    return [string[i:i + length] for i in range(0, len(string), length)]

with open('input.txt', 'r') as file:
    data = file.read()
    dataSplit = data.split(",")
    total = 0
    for item in dataSplit:
        rangeSplit = item.split("-")
        low = int(rangeSplit[0])
        high = int(rangeSplit[1])
        for num in range(low, high + 1):
            if (isInvalid(num)):
                total += num
    print(total)
