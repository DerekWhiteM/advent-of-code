'''
--- Day 4: Part Two ---
'''

# Load into a 2D array
matrix = []
rows = 0 # cols is the same
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))
        rows += 1 

def checkDiagonalUp(i, j):
    r1 = i + 1
    r2 = i - 1
    c1 = j + 1
    c2 = j - 1
    if (r1 < 0 or r1 >= rows): return False
    if (r2 < 0 or r2 >= rows): return False
    if (c1 < 0 or c1 >= rows): return False
    if (c2 < 0 or c2 >= rows): return False
    return (matrix[r1][c1] == 'M' and matrix[r2][c2] == 'S') or (matrix[r1][c1] == 'S' and matrix[r2][c2] == 'M')

def checkDiagonalDown(i, j):
    r1 = i - 1
    r2 = i + 1
    c1 = j + 1
    c2 = j - 1
    if (r1 < 0 or r1 >= rows): return False
    if (r2 < 0 or r2 >= rows): return False
    if (c1 < 0 or c1 >= rows): return False
    if (c2 < 0 or c2 >= rows): return False
    return (matrix[r1][c1] == 'M' and matrix[r2][c2] == 'S') or (matrix[r1][c1] == 'S' and matrix[r2][c2] == 'M')

# Iterate through each character
sum = 0
for i in range(rows):
    for j in range(rows):
        char = matrix[i][j]
        if char != 'A': 
            continue
        if checkDiagonalDown(i, j) and checkDiagonalUp(i, j): 
            sum += 1

print(sum)
        