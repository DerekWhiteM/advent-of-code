'''
--- Day 4: Part One ---
'''

target = 'XMAS'

# Load into a 2D array
matrix = []
rows = 0 # cols is the same
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))
        rows += 1 

def checkHorizontal(i, j):
    substring = ''
    for col in range(j, rows):
        substring += matrix[i][col]
        if substring == target: return True
        if substring in target: continue
        return False
    
def checkHorizontalBackwards(i, j):
    substring = ''
    for col in range(j, -1, -1):
        substring += matrix[i][col]
        if substring == target: return True
        if substring in target: continue
        return False
    
def checkVertical(i, j):
    substring = ''
    for row in range(i, rows):
        substring += matrix[row][j]
        if substring == target: return True
        if substring in target: continue
        return False
    
def checkVerticalBackwards(i, j):
    substring = ''
    for row in range(i, -1, -1):
        substring += matrix[row][j]
        if substring == target: return True
        if substring in target: continue
        return False

def checkDiagonalDown(i, j):
    substring = ''
    shift = 0
    for row in range(i, rows):
        if (j + shift >= rows):
            return False
        substring += matrix[row][j + shift]
        shift += 1
        if substring == target: return True
        if substring in target: continue
        return False
    
def checkDiagonalUpBackwards(i, j):
    substring = ''
    shift = 0
    for row in range(i, -1, -1):
        if (j + shift >= rows):
            return False
        substring += matrix[row][j + shift]
        shift += 1
        if substring == target: return True
        if substring in target: continue
        return False
    
def checkDiagonalUp(i, j):
    substring = ''
    shift = 0
    for row in range(i, rows):
        if (j - shift < 0):
            return False
        substring += matrix[row][j - shift]
        shift += 1
        if substring == target: return True
        if substring in target: continue
        return False

def checkDiagonalDownBackwards(i, j):
    substring = ''
    shift = 0
    for row in range(i, -1, -1):
        if (j - shift < 0):
            return False
        substring += matrix[row][j - shift]
        shift += 1
        if substring == target: return True
        if substring in target: continue
        return False

# Iterate through each character
sum = 0
for i in range(rows):
    for j in range(rows):
        char = matrix[i][j]
        if char != target[0]: continue
        if checkHorizontal(i, j): sum += 1
        if checkVertical(i, j): sum += 1
        if checkDiagonalDown(i, j): sum += 1
        if checkDiagonalUp(i, j): sum += 1
        if checkHorizontalBackwards(i, j): sum += 1
        if checkVerticalBackwards(i, j): sum += 1
        if checkDiagonalDownBackwards(i, j): sum += 1
        if checkDiagonalUpBackwards(i, j): sum += 1

print(sum)
        