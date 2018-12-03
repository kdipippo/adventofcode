def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines

def linesToDictionary(lines):
  programs = {}
  for i in range(len(lines)):
    children = []
    for j in range(2,len(lines[i])):
      children.append(lines[i][j].replace(",",""))
    programs[lines[i][0]] = children
  return programs

nodeList = []
def part1(programs, currNode):
  nodeList = []
  searchTree(currNode,nodeList,programs)
  return nodeList

def searchTree(currNode, nodeList, programs):
  if currNode not in nodeList:
    nodeList.append(currNode)
  for i in range(0,len(programs[currNode])):
    if programs[currNode][i] not in nodeList:
      searchTree(programs[currNode][i],nodeList,programs)

def part2(programs):
  groupList = []
  keys = programs.keys()
  for key in keys:
    currGroup = part1(programs,key)
    groupList.append(groupToStr(currGroup))
  groupCounts = {}
  for i in range(len(groupList)):
    if groupList[i] in groupCounts:
      groupCounts[groupList[i]] += 1
    else:
      groupCounts[groupList[i]] = 1
  gKeys = groupCounts.keys();
  for i in range(len(gKeys)):
    print gKeys[i]
  return len(gKeys)

def groupToStr(group):
  group.sort()
  groupStr = ""
  for i in range(len(group)):
    groupStr += str(group[i]) + ","
  return groupStr

if __name__ == "__main__":
  inputs = readfileintowords("input.txt")
  programs = linesToDictionary(inputs)
  print part2(programs)
