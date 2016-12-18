import time

class Disc:
    def __init__(self, name, allPos, startPos):
        self.name = name
        self.allPos = allPos
        self.currPos = startPos
    def printDiscInfo(self):
        return str(self.name) + ": " + str(self.allPos) + " " + str(self.currPos)
    def printDisc(self):
        discOutput = ['-']*self.allPos
        discOutput[self.currPos] = 'O'
        return "".join(discOutput)
    def move(self):
        self.currPos = (self.currPos + 1) % self.allPos
    def futureMoves(self, incr):
        return (self.currPos + incr) % self.allPos

# --------------------------------------------------------

# takes in a file name and returns the contents of file
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def createDisc(inputStr):
    # 'Disc #1 has 5 positions; at time=0, it is at position 4.'
    inputList = inputStr.split(' ')
    name = int(inputList[1].replace('#',''))
    allPos = int(inputList[3])
    currPos = int(inputList[-1].replace('.',''))
    return Disc(name,allPos,currPos)

def testCapsuleDrop(discs):
    for i in range(len(discs)):
        if discs[i].futureMoves(i+1) != 0:
            return False
    return True

def part1(formattedInput):
    discs = []
    for i in range(len(formattedInput)):
        discs.append(createDisc(formattedInput[i]))
    timeCount = 0
    discs.append(Disc(999,11,0))
    while True:
        if testCapsuleDrop(discs):
            return timeCount
        for i in range(len(discs)):
            discs[i].move()
        #time.sleep(1)
        timeCount += 1

if __name__ == "__main__":
    tInput = formatInput('testinput.txt')
    dInput = formatInput('input.txt')
    print part1(dInput)
