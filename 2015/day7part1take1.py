import numpy as np

# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def retWires(wires,inList,index):
    if inList[index] in wires:
        return np.uint16(wires[inList[index]])
    else:
        return np.uint16(index)

def parseInput(inputstr, wires):
    inputList = inputstr.split(' ')
    #print inputList
    if len(inputList) == 5:
        #[letter,'ACTION',num,'->',letter]
        if inputList[1] == 'LSHIFT':
            wires[inputList[-1]] = retWires(wires,inputList,0) << int(inputList[2])
        elif inputList[1] == 'RSHIFT':
            wires[inputList[-1]] = retWires(wires,inputList,0) >> int(inputList[2])
        elif inputList[1] == 'AND':
            wires[inputList[-1]] = retWires(wires,inputList,0) & retWires(wires,inputList,2)
        elif inputList[1] == 'OR':
            wires[inputList[-1]] = retWires(wires,inputList,0) | retWires(wires,inputList,2)
    elif 'NOT' in inputstr:
        # ['NOT',num/letter,'->',letter]
        if not inputList[1].isdigit():
            wires[inputList[-1]] = - retWires(wires,inputList,1)
        else:
            wires[inputList[-1]] = - int(inputList[1])
        while wires[inputList[-1]] < 0:
            wires[inputList[-1]] += 65535
    else: # assignment
        # [num/letter,'->',letter]
        if not inputList[0].isdigit():
            wires[inputList[-1]] = 65535 - retWires(wires,inputList,0)
        else:
            wires[inputList[-1]] = int(inputList[0])
    #print wires
    #print ""
    return wires

def parseCommands(commands):
    wires = {}
    for i in range(len(commands)):
        wires = parseInput(commands[i],wires)
    return wires

if __name__ == "__main__":
    #print parseCommands(formatInput('testinput.txt'))
    print parseCommands(formatInput('input.txt'))['a']
    
