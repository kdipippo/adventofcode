# returns contents of a file
def formatInput(filename):
    triangles = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def getIndex(parts):
    splitparts = parts[2].split("=")
    return int(splitparts[1])

def parseInput(screen,line):
    parts = line.split(" ")
    if len(parts) == 2 and parts[0] == 'rect':
        # rect AxB
        aANDb = map(int,parts[1].split('x')) # [A,B]
        for i in range(aANDb[1]):
            for j in range(aANDb[0]):
                screen[i][j] = '#'
    elif parts[0] == 'rotate' and parts[1] == 'row':
        # rotate row y=A by B
        rowIndex = getIndex(parts) #A
        shiftValue = int(parts[-1])
        for i in range(shiftValue):
            screen[rowIndex].insert(0, screen[rowIndex].pop(-1))
    elif parts[0] == 'rotate' and parts[1] == 'column':
        # rotate column y=A by B
        colIndex = getIndex(parts) #A
        shiftValue = int(parts[-1])
        # assemble column
        colList = []
        for i in range(len(screen)):
            colList.append(screen[i][colIndex])
        # shift column
        for i in range(shiftValue):
            colList.insert(0, colList.pop(-1))
        # mutate strings to accomodate change
        for i in range(len(screen)):
            screen[i][colIndex] = colList[i]
    return screen

def makeScreen(width,height):
    screenPixels = []
    for i in range(height):
        screenPixels.append(['.']*width)
    return screenPixels

def printScreen(screen):
    for i in range(len(screen)):
        print "".join(screen[i])

def part1(width,height,filename):
    commands = formatInput(filename)
    screen = makeScreen(width,height)
    for i in range(len(commands)):
        screen = parseInput(screen,commands[i])
    litCount = 0
    printScreen(screen)
    for i in range(len(screen)):
        litCount += screen[i].count('#')
    return litCount
        

# ==================================================
if __name__ == "__main__":
    DEBUG = False
    if DEBUG:
        screen = makeScreen(7,3)
        screen = parseInput(screen,'rect 3x2')
        screen = parseInput(screen,'rotate column x=1 by 1')
        screen = parseInput(screen,'rotate row y=0 by 4')
        printScreen(screen)
        print ""
        screen = parseInput(screen,'rotate column x=1 by 1')
        printScreen(screen)

    print part1(50,6,'input.txt')
    
    
