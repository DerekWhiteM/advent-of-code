class Dial:

    NUM_POSITIONS = 100

    def __init__(self, position):
        self.position = position

    def rotateLeft(self, num):
        self.position = (self.position - num) % (self.NUM_POSITIONS)
        return self.position
    
    def rotateRight(self, num):
        self.position = (self.position + num) % (self.NUM_POSITIONS)
        return self.position

dial = Dial(50)
countZeros = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        cmdDir = line[0]
        cmdNum = int(line[1:])
        result = None
        match cmdDir:
            case 'R':
                result = dial.rotateRight(cmdNum)
            case 'L':
                result = dial.rotateLeft(cmdNum)
            case _:
                raise Exception('Unknown command:', cmdDir)
        if result == 0:
            countZeros += 1

print(countZeros) # Output -> 989