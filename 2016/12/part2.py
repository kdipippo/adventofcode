# returns contents of a file
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def makeDict():
    assembunny = {}
    assembunny['a'] = 0
    assembunny['b'] = 0
    assembunny['c'] = 1
    assembunny['d'] = 0
    return assembunny

def readInstruct(instructStr,assembunny):
    instructList = instructStr.split(" ")
    retVal = 1
    if instructList[0] == 'cpy':
        val = 0
        if instructList[1].isdigit():
            val = int(instructList[1])
        else:
            val = int(assembunny[instructList[1]])
        assembunny[instructList[2]] = val
    elif instructList[0] == 'inc':
        assembunny[instructList[1]] += 1
    elif instructList[0] == 'dec':
        assembunny[instructList[1]] -= 1
    elif instructList[0] == 'jnz':
        val = 0
        if instructList[1].isdigit():
            val = int(instructList[1])
        else:
            val = int(assembunny[instructList[1]])
        if val != 0:
            retVal = int(instructList[2])
    return retVal, assembunny

def part1(inputList):
    assembunny = makeDict()
    currentIndex = 0
    while currentIndex < len(inputList):
        retVal, assembunny = readInstruct(inputList[currentIndex],assembunny)
        currentIndex += retVal
    return assembunny

# ==================================================
if __name__ == "__main__":
    test = formatInput('testinput.txt')
    instructions = formatInput('input.txt')
    print part1(instructions)
