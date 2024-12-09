num_safe = 0

with open('input.txt', 'r') as file:
    for line in file:
        columns = line.split()
        asc = True
        valid = True
        last = int(columns[0])
        for i in range(1, len(columns)):
            current = int(columns[i])

            # Set asc/desc
            if i == 1:
                asc = current > last

            # Check direction
            if asc:
                if (current < last):
                    valid = False
                    break
            else:
                if (current > last):
                    valid = False
                    break

            # Check if gradual
            diff = abs(current - last)
            if diff > 3 or diff < 1:
                valid = False
                break

            last = current
        
        if valid:
            num_safe += 1

print(num_safe)