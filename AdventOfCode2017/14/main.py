from array import array

# START OF DAY 10 =================
def convertstrtobytearray(inputStr):
  bytes = array("B",inputStr)
  finalBytes = []
  for i in range(len(bytes)):
    finalBytes.append(bytes[i])
  suffixBytes = [17, 31, 73, 47, 23]
  for i in range(len(suffixBytes)):
    finalBytes.append(suffixBytes[i])
  return finalBytes

def knotHashRound(lengths,klist,kcurrPos,kskipSize):
  for i in range(len(lengths)):
    sublist = []
    for j in range(kcurrPos,kcurrPos+lengths[i]):
      sublist.append(klist[j%len(klist)])
    sublist.reverse()
    sublistCount = 0
    for j in range(kcurrPos,kcurrPos+lengths[i]):
      klist[j%len(klist)] = sublist[sublistCount]
      sublistCount += 1
    kcurrPos += lengths[i] + kskipSize
    kcurrPos %= len(klist)
    kskipSize += 1
  return klist,kcurrPos,kskipSize

def sparseToDense(sparseHash):
  denseHash = []
  for i in range(0,16):
    denseVal = sparseHash[16*i]
    for j in range(1,16):
      denseVal ^= sparseHash[16*i + j]
    denseHash.append(denseVal)
  return denseHash

def denseToHex(denseHash):
  hexStr = ""
  for i in range(len(denseHash)):
    temp = str(hex(denseHash[i]))[2:]
    if len(temp) == 1:
      temp = "0" + temp
    hexStr += temp
  return hexStr

def knotHash(inputStr,klist):
  stream = convertstrtobytearray(inputStr)
  kcurrPos = 0
  kskipSize = 0
  for i in range(0,64):
    klist,kcurrPos,kskipSize = knotHashRound(stream,klist,kcurrPos,kskipSize)
  sparseHash = list(klist)
  denseHash = sparseToDense(sparseHash)
  return denseToHex(denseHash)
# END OF DAY 10 ===================

def getUsedCount(currHash):
  binHash = str(bin(int(currHash, 16))[2:])
  printBinHash(binHash)
  #print binHash.count("1"),
  return binHash.count("1")

def printBinHash(binHash):
  binHash = binHash.replace("1","#")
  binHash = binHash.replace("0",".")
  while len(binHash) < 128:
    binHash = "." + binHash
  print binHash

def getGridRow(currHash):
  binHash = str(bin(int(currHash, 16))[2:])
  binHash = binHash.replace("1","#")
  binHash = binHash.replace("0",".")
  while len(binHash) < 128:
    binHash = "." + binHash
  return list(binHash)

def part1(inputStr):
  startklist = []
  count = 0
  for i in range(0, 256):
    startklist.append(i)
  for i in range(128):
    klist = startklist[:]
    currHash = knotHash(inputStr + "-" + str(i),klist)
    count += getUsedCount(currHash)
  print count

def part2(inputStr):
  startklist = []
  grid = []
  for i in range(0, 256):
    startklist.append(i)
  for i in range(128):
    klist = startklist[:]
    currHash = knotHash(inputStr + "-" + str(i),klist)
    grid.append(getGridRow(currHash))
  print "Regionalizing grid..."
  regionalizeGrid(grid)

def regionalizeGrid(grid):
  regionNum = 1
  for i in range(len(grid)):
    for j in range(len(grid)):
      surroundingRegionsPresent = getSurroundingRegions(grid,i,j)

      # there are multiple clashing Regions
      if len(surroundingRegionsPresent) > 1 and grid[i][j] != ".":
        # replace all occurrences of the secondary surrounding regions with the first
        dominatingRegion = surroundingRegionsPresent[0]
        grid = fillSurroundingCells(grid,i,j,dominatingRegion)
        for s in range(1,len(surroundingRegionsPresent)):
          grid = replaceSubmissiveRegions(grid,surroundingRegionsPresent[s],dominatingRegion)
      else:
        surroundingRegionPresent = surroundingRegionsPresent[0]
        # we find a used cell and have an ajacent number
        if grid[i][j] == "#" and surroundingRegionPresent != "0":
          grid = fillSurroundingCells(grid,i,j,surroundingRegionPresent)

        # we are at a region number and need to fill surrounding cells
        elif grid[i][j] != "#" and grid[i][j] != ".":
          grid = fillSurroundingCells(grid,i,j,grid[i][j])

        # we find a used cell without an adjacent number
        elif grid[i][j] == "#":
          grid = fillSurroundingCells(grid,i,j,str(regionNum))
          regionNum += 1
  regionNums = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] != "." and int(grid[i][j]) not in regionNums:
        regionNums.append(int(grid[i][j]))
  numDigits = len(str(max(regionNums)))
  printRegionalizedGrid(grid,numDigits)
  print "There are " + str(len(regionNums)) + " regions"


def printRegionalizedGrid(grid,numDigits):
  for i in range(len(grid)/8):
    for j in range(len(grid[i])/8):
      if grid[i][j] == ".":
        print " "*(numDigits-1) + ".",
      else:
        tempStr = grid[i][j]
        while len(tempStr) < numDigits:
          tempStr = " " + tempStr
        print tempStr,
    print

def getSurroundingRegions(grid,cellX,cellY):
  surroundingRegions = []
  if cellX > 0:
    if grid[cellX-1][cellY] != "#" and grid[cellX-1][cellY] != ".":
      if grid[cellX-1][cellY] not in surroundingRegions:
        surroundingRegions.append(grid[cellX-1][cellY])
  if cellX < len(grid)-1:
    if grid[cellX+1][cellY] != "#" and grid[cellX+1][cellY] != ".":
      if grid[cellX+1][cellY] not in surroundingRegions:
        surroundingRegions.append(grid[cellX+1][cellY])
  if cellY > 0:
    if grid[cellX][cellY-1] != "#" and grid[cellX][cellY-1] != ".":
      if grid[cellX][cellY-1] not in surroundingRegions:
        surroundingRegions.append(grid[cellX][cellY-1])
  if cellY < len(grid)-1:
    if grid[cellX][cellY+1] != "#" and grid[cellX][cellY+1] != ".":
      if grid[cellX][cellY+1] not in surroundingRegions:
        surroundingRegions.append(grid[cellX][cellY+1])
  if len(surroundingRegions) == 0:
    surroundingRegions.append("0")
  return surroundingRegions

def fillSurroundingCells(grid,cellX,cellY,regionName):
  grid[cellX][cellY] = regionName
  if cellX > 0:
    if grid[cellX-1][cellY] == "#":
      grid[cellX-1][cellY] = regionName
  if cellX < len(grid)-1:
    if grid[cellX+1][cellY] == "#":
      grid[cellX+1][cellY] = regionName
  if cellY > 0:
    if grid[cellX][cellY-1] == "#":
      grid[cellX][cellY-1] = regionName
  if cellY < len(grid)-1:
    if grid[cellX][cellY+1] == "#":
      grid[cellX][cellY+1] = regionName
  return grid

def replaceSubmissiveRegions(grid,submissive,dominant):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == submissive:
        grid[i][j] = dominant
  return grid

if __name__ == "__main__":
  puzz = "jzgqcdpd"
  test = "flqrgnkx"
  smolGrid = [['#', '#', '.', '#', '.', '#', '.', '.'], ['.', '#', '.', '#', '.', '#', '.', '#'], ['.', '.', '.', '.', '#', '.', '#', '.'], ['#', '.', '#', '.', '#', '#', '.', '#'], ['.', '#', '#', '.', '#', '.', '.', '.'], ['#', '#', '.', '.', '#', '.', '.', '#'], ['.', '#', '.', '.', '.', '#', '.', '.'], ['#', '#', '.', '#', '.', '#', '#', '.']]
  #regionalizeGrid(smolGrid)
  part2(puzz)
