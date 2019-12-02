import time

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def readfileintowords(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def getClosetCoord(currX, currY, coords):
    print("sup")

def part1(inputs):
    maxX = 0
    maxY = 0
    coords = {}
    for coord in inputs:
        currCoord = coord.split(", ")
        currX = int(currCoord[0])
        currY = int(currCoord[1])
        if (currX > maxX):
            maxX = currX
        if (currY > maxY):
            maxY = currY
        coords[coord] = Coord(currX, currY)
    print(str(maxX) + ", " + str(maxY))
    for y in range(maxY+1):
        currRow = ""
        for x in range(maxX+1):
            if str(x)+", "+str(y) in coords:
                currRow += "#"
            else:
                currRow += "."
        print(currRow)

if __name__ == "__main__":
    inputs = readfileintowords("test.txt")
    start = time.time()
    part1(inputs)
    end = time.time()
    print(end - start)
