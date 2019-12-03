import sys

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def getPath(wire):
  lines = wire.split(",")
  paths = set()
  i = [0,0]
  for line in lines:
    if line[0] == "U":
      index = 1
      modifier = 1
    elif line[0] == "D":
      index = 1
      modifier = -1
    elif line[0] == "L":
      index = 0
      modifier = -1
    elif line[0] == "R":
      index = 0
      modifier = 1
    length = int(line[1:])
    for l in range(length):
      i[index] += modifier
      coord = str(i[0]) + ":" + str(i[1])
      if coord not in paths:
        paths.add(coord)
  return paths

def getIntersections(wires):
  path1 = getPath(wires[0])
  path2 = getPath(wires[1])
  intersections = path1.intersection(path2)
  min = sys.maxint
  print intersections
  for intersection in intersections:
    vals = intersection.split(":")
    manhattan = abs(int(vals[0])) + abs(int(vals[1]))
    if manhattan < min:
      min = manhattan
  return min

if __name__ == "__main__":
  # get the points that the path gets
  wires = readfileintowords("input.txt")
  test1 = ["R8,U5,L5,D3","U7,R6,D4,L4"]
  test2 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]
  test3 = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
  # print getIntersections(test1)
  print getIntersections(test2)
  print getIntersections(test3)
  print getIntersections(wires)