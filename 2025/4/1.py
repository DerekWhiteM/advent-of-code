matrix = []

def getNumAdjacent(row, col):
    maxRowIdx = len(matrix) - 1
    maxColIdx = len(matrix[0]) - 1

    aboveLeft = matrix[row-1][col-1] if row > 0 and col > 0 else None
    above = matrix[row-1][col] if row > 0 else None
    aboveRight = matrix[row-1][col+1] if row > 0 and col < maxColIdx else None 
    right = matrix[row][col+1] if col < maxColIdx else None
    belowRight = matrix[row+1][col+1] if row < maxRowIdx and col < maxColIdx else None
    below = matrix[row+1][col] if row < maxRowIdx else None
    belowLeft = matrix[row+1][col-1] if row < maxRowIdx and col > 0 else None
    left = matrix[row][col-1] if col > 0 else None

    adjacentTiles = [aboveLeft, above, aboveRight, right, belowRight, below, belowLeft, left]

    numAdjacentTiles = 0

    for tile in adjacentTiles:
        if (tile == '@'):
            numAdjacentTiles += 1

    return numAdjacentTiles

with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))
    print(getNumAdjacent(0, 3))
