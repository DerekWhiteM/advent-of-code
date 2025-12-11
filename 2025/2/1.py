def isInvalid(num):
    num = str(num)
    strLen = len(num)
    if (strLen % 2 != 0):
        return False
    midpoint = strLen // 2
    firstHalf = num[:midpoint]
    secondHalf = num[midpoint:]
    if (firstHalf == secondHalf):
        return True
    return False

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
