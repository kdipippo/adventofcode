import sys

class Planet:
  def __init__(self, name):
    self.name = name
    self.leftOrbit = None
    self.rightOrbits = []
  def getName(self):
    return self.name
  def leftOrbitExists(self):
    if not self.leftOrbit:
      return False
    return True
  def getLeftOrbitName(self):
    return self.leftOrbit.getName()
  def setLeftOrbit(self, otherPlanet):
    self.leftOrbit = otherPlanet
  def addRightOrbit(self, otherPlanet):
    self.rightOrbits.append(otherPlanet)
  def printPlanet(self):
    if not self.leftOrbit:
      leftName = "None"
    else:
      leftName = str(self.leftOrbit.getName())
    result = str(self.name) + "\t" + leftName + "\t"
    for planet in self.rightOrbits:
      result += planet.getName() + ","
    print(result)

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def debugPlanets(planets):
  for planetName in planets.keys():
    planets[planetName].printPlanet()

def parseOrbits(inputs):
  planets = dict()
  for input in inputs:
    left,right = input.split(")")
    if left not in planets:
      leftPlanet = Planet(left)
      planets[left] = leftPlanet
    else:
      leftPlanet = planets[left]
    if right not in planets:
      rightPlanet = Planet(right)
      planets[right] = rightPlanet
    else:
      rightPlanet = planets[right]
    rightPlanet.setLeftOrbit(leftPlanet)
    leftPlanet.addRightOrbit(rightPlanet)
  return planets

def getOrbitCounts(inputs):
  planets = parseOrbits(inputs)
  totalCount = 0
  for planetName in planets.keys():
    currPlanetName = planetName
    currCount = 0
    while planets[currPlanetName].leftOrbitExists():
      currCount += 1
      currPlanetName = planets[currPlanetName].getLeftOrbitName()
    totalCount += currCount
  print(totalCount)

def getPlanetPath(planets, nodeName):
  currPlanetName = nodeName
  planetPath = []
  while planets[currPlanetName].leftOrbitExists():
    planetPath.append(currPlanetName)
    currPlanetName = planets[currPlanetName].getLeftOrbitName()
  # result = "->".join(planetPath)
  # print(result)
  return planetPath

def groundControlToMajorTom(inputs):
  planets = parseOrbits(inputs)
  YOUplanetPath = getPlanetPath(planets, "YOU")
  YOUplanetSet = set(YOUplanetPath)
  SANplanetPath = getPlanetPath(planets, "SAN")
  SANplanetSet = set(SANplanetPath)
  intersections = list(YOUplanetSet.intersection(SANplanetSet))
  # find the closest intersection
  minDist = sys.maxint
  currIntersection = ""
  for intersection in intersections:
    YOUdist = YOUplanetPath.index(intersection) - 1
    SANdist = SANplanetPath.index(intersection) - 1
    currDist = YOUdist + SANdist
    if currDist < minDist:
      minDist = currDist
      currIntersection = intersection
  print(currIntersection + ": " + str(minDist))


if __name__ == "__main__":
  # inputs = readfileintowords("test2.txt")
  # groundControlToMajorTom(inputs)
  inputs = readfileintowords("input.txt")
  groundControlToMajorTom(inputs)