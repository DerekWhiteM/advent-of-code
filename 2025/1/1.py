class Dial:

    MAX = 99

    def __init__(self, start):
        self.start = start
        self.current = start

    def rotateLeft(self, num):
        self.current = (self.current - num) % (self.MAX + 1)
        return self.current
    
    def rotateRight(self, num):
        self.current = (self.current + num) % (self.MAX + 1)
        return self.current

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