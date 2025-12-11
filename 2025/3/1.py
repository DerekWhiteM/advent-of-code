with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        bank = list(line)
        print(bank)