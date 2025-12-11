with open('input.txt', 'r') as file:
    data = file.read()
    dataSplit = data.split(",")
    for range in dataSplit:
        rangeSplit = range.split("-")
        low = rangeSplit[0]
        high = rangeSplit[1]
        print(low, high)
