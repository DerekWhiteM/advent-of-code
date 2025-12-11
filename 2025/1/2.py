class Dial:

    NUM_POSITIONS = 100
    timesPassedZero = 0

    def __init__(self, position):
        self.position = position

    def left(self, num):
        total = self.position - num
        if self.position == 0:
            self.timesPassedZero += (abs(total) // self.NUM_POSITIONS)
        elif total < 0:
            self.timesPassedZero += ((abs(total) + (self.NUM_POSITIONS - 1)) // self.NUM_POSITIONS)
        self.position = total % self.NUM_POSITIONS
        if self.position == 0:
            self.timesPassedZero += 1
    
    def right(self, num):
        total = self.position + num
        self.position = total % self.NUM_POSITIONS
        self.timesPassedZero += (total // self.NUM_POSITIONS)

dial = Dial(50)

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        cmdDir = line[0]
        cmdNum = int(line[1:])
        match cmdDir:
            case 'R':
                dial.right(cmdNum)
            case 'L':
                dial.left(cmdNum)
            case _:
                raise Exception('Unknown command:', cmdDir)

print(dial.timesPassedZero)
