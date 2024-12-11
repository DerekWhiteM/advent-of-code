def processUpdate(columns, isCorrect):
    # Store the update in a dictionary (hash map) so we can quickly get the index of each page
    update = {}
    for i in range(len(columns)):
        update[columns[i]] = i
    # Validate each rule
    for rule in rules:
        index1 = update.get(rule[0])
        index2 = update.get(rule[1])
        if (index1 == None or index2 == None):
            continue
        if index1 > index2:
            # Swap the values and try again
            temp = columns[index2]
            columns[index2] = columns[index1]
            columns[index1] = temp
            return processUpdate(columns, False)
    return 0 if isCorrect else int(columns[int(len(update) / 2)])

with open('input.txt', 'r') as file:
    sum = input_section = 0
    rules = []
    for line in file:
        if line == '\n':
            input_section = 1
            continue
        if input_section == 0:
            columns = (line.strip()).split('|')
            rules.append([columns[0], columns[1]])
        else:
            columns = (line.strip()).split(',')
            sum += processUpdate(columns, True)
    print(sum)