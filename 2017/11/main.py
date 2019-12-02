def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines[0][0].split(",")

def part2(instructions):
  coordX = 0
  coordY = 0
  max = 0
  for i in range(len(instructions)):
    if instructions[i] == 'n':
      coordX += 0
      coordY += 2
    elif instructions[i] == 'ne':
      coordX += 1
      coordY += 1
    elif instructions[i] == 'e':
      coordX += 2
      coordY += 0
    elif instructions[i] == 'se':
      coordX += 1
      coordY += -1
    elif instructions[i] == 's':
      coordX += 0
      coordY += -2
    elif instructions[i] == 'sw':
      coordX += -1
      coordY += -1
    elif instructions[i] == 'w':
      coordX += -2
      coordY += 0
    elif instructions[i] == 'nw':
      coordX += -1
      coordY += 1
    if getDist(coordX,coordY) > max:
      max = getDist(coordX,coordY)
  #return getDist(coordX,coordY)
  return max

def getDist(coordX,coordY):
  dist = abs(coordX) + abs(coordY)
  return dist/2

if __name__ == "__main__":
  instructions = readfileintowords("input.txt")
  test1 = ['ne','ne','ne']
  test2 = ['ne','ne','sw','sw']
  test3 = ['ne','ne','s','s']
  test4 = ['se','sw','se','sw','sw']
  print part2(test1)
  print part2(test2)
  print part2(test3)
  print part2(test4)
  print part2(instructions)
