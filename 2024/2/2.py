def check_report(report):
    asc = True
    valid = True
    last = int(report[0])
    for i in range(1, len(report)):
        current = int(report[i])
        if i == 1:
            asc = current > last
        if asc:
            if (current < last):
                valid = False
                break
        else:
            if (current > last):
                valid = False
                break
        diff = abs(current - last)
        if diff > 3 or diff < 1:
            valid = False
            break
        last = current
    return valid

def problem_dampener(report):
    safe = check_report(report)
    if safe:
        return True
    for i in range(len(report)):
        copy = report[:]
        copy.pop(i)
        safe = check_report(copy)
        if safe:
            return True
    return False

with open('input.txt', 'r') as file:
    num_safe = 0
    for line in file:
        report = line.split()
        safe = problem_dampener(report)
        if safe:
            num_safe += 1
    print(num_safe)
