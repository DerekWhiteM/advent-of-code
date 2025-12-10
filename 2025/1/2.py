class Dial:

    NUM_POSITIONS = 100

    timesPassedZero = 0

    def __init__(self, position):
        self.position = position

    def left(self, num):
        total = self.position - num
        self.position = total % self.NUM_POSITIONS
        if total < 0:
            self.timesPassedZero += (abs(total) + 100) // self.NUM_POSITIONS
        elif total == 0:
            self.timesPassedZero += 1
        print(self.timesPassedZero)
    
    def right(self, num):
        total = self.position + num
        self.position = total % self.NUM_POSITIONS
        self.timesPassedZero += total // self.NUM_POSITIONS
        print(self.timesPassedZero)

dial = Dial(50)

dial.left(68)
dial.left(30)
dial.right(48)
dial.left(5)
dial.right(60)
dial.left(55)
dial.left(1)
dial.left(99)
dial.right(14)
dial.left(82)

'''
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
'''
