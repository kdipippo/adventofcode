# Welcome to John Conway's Game of Traps

# takes in a file name and returns the contents of file
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines[0]

def isTrap(importantTiles):
    if importantTiles == '^^.':
        return True
    if importantTiles == '.^^':
        return True
    if importantTiles == '^..':
        return True
    if importantTiles == '..^':
        return True
    return False

def genImportantTiles(rowBefore):
    importantTiles = []
    importantTiles.append('.' + rowBefore[:2])
    for i in range(1,len(rowBefore)-1):
        importantTiles.append(rowBefore[i-1]+rowBefore[i]+rowBefore[i+1])
    importantTiles.append(rowBefore[-2:] + '.')
    return importantTiles

def genRow(rowBefore):
    rowAfter = ''
    tiles = genImportantTiles(rowBefore)
    for i in range(len(tiles)):
        if isTrap(tiles[i]):
            rowAfter += '^'
        else:
            rowAfter += '.'
    return rowAfter

def genMap(firstRow,height):
    trapMap = []
    currRow = firstRow
    for i in range(height):
        trapMap.append(currRow)
        currRow = genRow(currRow)
    return trapMap

def printMap(trapMap):
    safeCount = 0
    for i in range(len(trapMap)):
        #print trapMap[i]
        safeCount += trapMap[i].count('.')
    print "-----" + str(safeCount)

if __name__ == "__main__":
    firstRow = formatInput('input.txt')
    printMap(genMap('..^^.',3))
    printMap(genMap('.^^.^.^^^^',10))
    printMap(genMap(firstRow,40))
    printMap(genMap(firstRow,400000))
