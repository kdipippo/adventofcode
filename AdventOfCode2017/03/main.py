def part1(squareNum):
  # find what a is, aka the range between which the power is
  a = getA(squareNum)
  #print "we got A: " + str(a)
  #print str(a) + "^2 to " + str(a+2) + "^2 has values: " + str((a+1)/2) + "-" + str(a+1)
  # start with a, go down until bottom of range is hit, then go up until number is reached
  downflag = True
  lower = (a+1)/2
  upper = a+1
  #print "LOWER = " + str(lower) + "; UPPER = " + str(upper)
  currentVal = a
  for i in range((a**2 + 1),squareNum):
    #print str(i) + ": " + str(currentVal)
    if downflag:
      currentVal -= 1
    else:
      currentVal += 1
    if currentVal == lower:
      downflag = False
    elif currentVal == upper:
      downflag = True
  result = str(squareNum) + " RESULT = " + str(currentVal)
  return result

def getA(num):
  i = 1
  while True:
    if i**2 < num and (i+2)**2 >= num:
      return i
    i+=2

def part2(num):
  power = 3
  grid = [[5,4,2],[10,1,1],[11,23,25]]
  printGrid(grid)
  grid,power = makeNewGrid(grid,power)
  printGrid(grid)
  #while doesGridContainsBlanks(grid):
  #if not doesGridContainsBlanks(grid):
  #  newGrid,newPower = makeNewGrid(grid,power)
  #printGrid(newGrid)

  # start at len(grid)-2,len(grid)-1 as starting point
  # get neighbors; add together if they are
  row = len(grid)-2
  col = len(grid)-1
  rightWall = True
  topWall = False
  leftWall = False
  bottomWall = False
  while True:
    if doesGridContainsBlanks(grid):
      result = addNeighbors(grid,row,col)
      if (result > num):
        return str(result) + "!!!!!!!"
      grid[row][col] = result
      printGrid(grid)
      if rightWall:
        row -= 1
      elif topWall:
        col -= 1
      elif leftWall:
        row += 1
      elif bottomWall:
        col += 1
      if row == 0 and col == (len(grid[0])-1):
        rightWall = False
        topWall = True
      elif row == 0 and col == 0:
        topWall = False
        leftWall = True
      elif row == (len(grid)-1) and col == 0:
        leftWall = False
        bottomWall = True
    else:
      grid,power = makeNewGrid(grid,power)
      row = len(grid)-2
      col = len(grid)-1
      rightWall = True
      topWall = False
      leftWall = False
      bottomWall = False


def doesGridContainsBlanks(grid):
  for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
      if grid[i][j] == ".":
        return True
  return False

def makeNewGrid(grid,power):
  newPower = power+2
  newGrid = []
  for i in range(0, newPower):
    newRow = []
    for j in range(0, newPower):
      newRow.append(".")
    newGrid.append(newRow)

  for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
      newGrid[i+1][j+1] = grid[i][j]
  return newGrid,newPower

def printGrid(grid):
  print "++++++++++++++++++++"
  for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
      if grid[i][j] < 10:
        print " " + str(grid[i][j]) + " ",
      else:
        print str(grid[i][j]) + " ",
    print ""
  print "++++++++++++++++++++"

def addNeighbors(grid,row,col):
  # get neighbors of current row,col cell
  vals = [-1,0,1]
  neighbors = []
  for i in range(0, len(vals)):
    for j in range(0, len(vals)):
      if isInsideGrid(grid,row+vals[i],col+vals[j]):
        neighbors.append(grid[row+vals[i]][col+vals[j]])
  sum = 0
  for i in range(len(neighbors)):
    if neighbors[i] != ".":
      sum += neighbors[i]
  return sum

def isInsideGrid(grid,row,col):
  if row < 0:
    return False
  if row >= len(grid):
    return False
  if col < 0:
    return False
  if col >= len(grid[0]):
    return False
  return True

if __name__ == "__main__":
  #print part1(12)
  #print part1(23)
  #print part1(1024)
  #print part1(368078)
  print part2(368078)
