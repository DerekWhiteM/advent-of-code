class Node:
    def __init__(self):
        self.up: Node = None
        self.right: Node = None
        self.down: Node = None
        self.left: Node = None
        self.visited: bool = False
        self.hasObstacle: bool = False

grid: list[list[Node]] = []
start: Node = None
sum = 0

# Put the nodes in a 2D array
with open('input.txt', 'r') as file:
    for line in file:
        row: list[Node] = []
        cols = line.strip()
        for col in cols:
            node = Node()
            if (col == '^'):
                start = node
            if (col == '#'):
                node.hasObstacle = True
            row.append(node)
        grid.append(row)
    
# Connect the nodes
num_rows = len(grid)
num_cols = len(grid[0])
for i in range(num_rows):
    for j in range(num_cols):
        # Link left/right
        if j > 0:
            grid[i][j].left = grid[i][j - 1]
        if j < num_cols - 1:
            grid[i][j].right = grid[i][j + 1]
        # Link up/down
        if i > 0:
            grid[i][j].up = grid[i - 1][j]
        if i < num_rows - 1:
            grid[i][j].down = grid[i + 1][j]
            
# Traverse the matrix
direction = 'up'
current = start
while True:
    match direction:
        case 'up':
            if current.up == None:
                break
            if current.up.hasObstacle:
                direction = 'right'
                continue
            current = current.up
        case 'right':
            if current.right == None:
                break
            if current.right.hasObstacle:
                direction = 'down'
                continue
            current = current.right
        case 'down':
            if current.down == None:
                break
            if current.down.hasObstacle:
                direction = 'left'
                continue
            current = current.down
        case 'left':
            if current.left == None:
                break
            if current.left.hasObstacle:
                direction = 'up'
                continue
            current = current.left
    if current.visited != True:
        current.visited = True
        sum += 1

print(sum)