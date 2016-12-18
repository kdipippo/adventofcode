# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def parseCommand(line):
    instructions = line.split(" ")
    coord1 = map(int,instructions[-3].split(","))
    coord2 = map(int,instructions[-1].split(","))
    for i in range(3):
        instructions.pop()
    return coord1,coord2,"".join(instructions)

def createLightGrid(size):
    lightGrid = []
    for i in range(size):
        lightGrid.append([0]*size)
    return lightGrid

def readCommand(lightGrid,line):
    coord1,coord2,instr = parseCommand(line)
    if instr == 'turnon':
        for x in range(coord1[0],coord2[0]+1):
            for y in range(coord1[1],coord2[1]+1):
                lightGrid[x][y] += 1
    elif instr == 'toggle':
        for x in range(coord1[0],coord2[0]+1):
            for y in range(coord1[1],coord2[1]+1):
                lightGrid[x][y] += 2
    elif instr == 'turnoff':
        for x in range(coord1[0],coord2[0]+1):
            for y in range(coord1[1],coord2[1]+1):
                if lightGrid[x][y] > 0:
                    lightGrid[x][y] -= 1
    return lightGrid

def printLightGrid(lightGrid):
    for i in range(len(lightGrid)):
        print "".join(map(str,lightGrid[i]))

def calcLightGrid(lightGrid):
    lightCount = 0
    for i in range(len(lightGrid)):
        lightCount += sum(lightGrid[i])
    return lightCount

if __name__ == "__main__":
    debug_flag = False
    if debug_flag:
        test1 = 'turn on 0,0 through 999,999'
        test2 = 'toggle 0,0 through 999,0'
        test3 = 'turn off 499,499 through 500,500'

        lightGrid = createLightGrid(1000)
        lightGrid = readCommand(lightGrid,test1)
        lightGrid = readCommand(lightGrid,test3)
        lightsOn = calcLightGrid(lightGrid)
        print "on:",lightsOn
        print "off:",1000*1000 - lightsOn

    lightGrid = createLightGrid(1000)
    instructions = formatInput('input.txt')
    for i in range(len(instructions)):
        lightGrid = readCommand(lightGrid,instructions[i])
    print calcLightGrid(lightGrid)
        
    
