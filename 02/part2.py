import numpy

# Keypad reordered so 7 is in the bottom-left corner
#KEYPAD = [[7,4,1],[8,5,2],[9,6,3]]
KEYPAD = [['-','-',5,'-','-'],
          ['-','A',6,2,'-'],
          ['D','B',7,3,1],
          ['-','C',8,4,'-'],
          ['-','-',9,'-','-']]

# takes in a file name
# returns a list of strings of form 'R#' or 'L#'
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def returnIndex(oldx,oldy,newx,newy):
    currentIndex = [newx,newy]
    currentIndex = numpy.clip(currentIndex,0,4) # fast way to keep values in range
    if getKeypadNum(currentIndex) == '-':
        currentIndex = [oldx,oldy]
    return currentIndex

def getCodeNumber(stringDirection, currentIndex):
    for i in range(len(stringDirection)):
        if stringDirection[i] == "U":
            currentIndex = returnIndex(currentIndex[0],currentIndex[1],currentIndex[0],currentIndex[1]+1)
        elif stringDirection[i] == "D":
            currentIndex = returnIndex(currentIndex[0],currentIndex[1],currentIndex[0],currentIndex[1]-1)
        elif stringDirection[i] == "R":
            currentIndex = returnIndex(currentIndex[0],currentIndex[1],currentIndex[0]+1,currentIndex[1])
        elif stringDirection[i] == "L":
            currentIndex = returnIndex(currentIndex[0],currentIndex[1],currentIndex[0]-1,currentIndex[1])
    return getKeypadNum(currentIndex), currentIndex

def getKeypadNum(currentIndex):
    return KEYPAD[currentIndex[0]][currentIndex[1]]

def assembleCode(directions):
    currentIndex = [1,1]
    for i in range(len(directions)):
        latestNum, currentIndex = getCodeNumber(directions[i], currentIndex)
        print latestNum,
    print ""

# ==================================================
if __name__ == "__main__":
    test1 = ["ULL","RRDDD","LURDL","UUUUD"]
    assembleCode(test1)
    
    code = formatInput('input.txt')
    assembleCode(code)
