from Tower import *

def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines

def createTowers(inputs):
  towers = []
  for i in range(len(inputs)):
    newTower = Tower(inputs[i][0],int(inputs[i][1][1:-1]),[])
    if len(inputs[i]) > 2:
      for j in range(3,len(inputs[i])):
        newTower.addChild((inputs[i][j]).replace(",",""))
    towers.append(newTower)
  return towers

def part1(towers):
  # get all the children from these nodes into one large array
  allChildren = []
  for i in range(len(towers)):
    newChildren = towers[i].getChildren()
    for j in range(len(newChildren)):
      if newChildren[j] not in allChildren:
        allChildren.append(newChildren[j])
  # iterate through towers, if they don't appear in children, then print
  for i in range(len(towers)):
    if towers[i].getName() not in allChildren:
      print "~~~~~~~~~~~~~~~~~~"
      print towers[i].getName()
  return 0

def part2(towers):
  # find all nodes with no children and sort by their parent nodes
  lastNodesObjects = []
  lastNodes = []
  for i in range(len(towers)):
    if len(towers[i].getChildren()) == 0:
      lastNodesObjects.append(towers[i])
      lastNodes.append(towers[i].getName())
  parentsOfLastNodes = []
  for i in range(len(towers)):
    if validParent(towers[i].getChildren(),lastNodes):
      fullString = towers[i].getName() + " (" + str(towers[i].getWeight()) + ") --- "
      for j in range(len(towers[i].getChildren())):
        fullString += printFullNode(towers[i].getChildren()[j],towers)
      print fullString
  return 0

def validParent(parentChildren, lastChildren):
  #print "######"
  #printTowers(parentChildren)
  #printTowers(lastChildren)
  #print "------"
  for i in range(len(parentChildren)):
    if parentChildren[i] in lastChildren:
      return True
  return False

def printFullNode(towerName,towers):
  for i in range(len(towers)):
    if (towers[i].getName() == towerName):
      return towers[i].getName() + " (" + str(towers[i].getWeight()) + ")"

def printTowers(towers):
  newStr = "["
  for i in range(len(towers)):
    newStr += "'" + towers[i].getName() + "', "
  newStr = newStr[:-1]
  newStr += "]"
  print newStr

def part2Take2(towers,startName):
  startName = "ykpsek"
  towerGrid = []


def gridTowerRecursion()


def getTower(towerName, towers):
  for i in range(len(towers)):
    if (towers[i].getName() == towerName):
      return towers[i]

if __name__ == "__main__":
  inputs = readfileintowords("input.txt")
  towers = createTowers(inputs)
  print part2(towers)
