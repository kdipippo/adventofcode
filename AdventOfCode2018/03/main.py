import time

def readfileintowords(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def parseClaim(claim):
    claim = claim.split(" ")    #['#1','@','1,3:','4x4']
    offset = claim[2].replace(":","").split(",")
    leftOffset = int(offset[0])
    topOffset = int(offset[1])
    dimensions = claim[3].split("x")
    width = int(dimensions[0])
    height = int(dimensions[1])
    return leftOffset,topOffset,width,height

def printFabric(fabric):
    for row in fabric:
        fabricrow = ""
        for thread in row:
            if thread == 0:
                fabricrow += "."
            else:
                fabricrow += str(thread)
        print(fabricrow)

def getOverlapFabricCount(fabric):
    overlapCount = 0
    for row in fabric:
        for thread in row:
            if thread >= 2:
                overlapCount += 1
    return overlapCount

def part1(inputs):
    number_cols = 1000
    number_rows = 1000
    fabric = [[0] * number_cols for i in range(number_rows)]
    for claim in inputs:
        leftOffset,topOffset,width,height = parseClaim(claim)
        for c in range(leftOffset, width+leftOffset):
            for r in range(topOffset, height+topOffset):
                fabric[r][c] += 1
    #printFabric(fabric)
    print(getOverlapFabricCount(fabric))

def claimDoesOverlap(fabric, claim):
    leftOffset,topOffset,width,height = parseClaim(claim)
    for c in range(leftOffset, width+leftOffset):
        for r in range(topOffset, height+topOffset):
            if (fabric[r][c] >= 2):
                return True
    return False

def part2(inputs):
    number_cols = 1000
    number_rows = 1000
    fabric = [[0] * number_cols for i in range(number_rows)]
    intermediateClaims = [] #store claims if they don't have an overlap yet
    for claim in inputs:
        leftOffset,topOffset,width,height = parseClaim(claim)
        overlapFlag = False
        for c in range(leftOffset, width+leftOffset):
            for r in range(topOffset, height+topOffset):
                if (fabric[r][c] > 0):
                    overlapFlag = True
                fabric[r][c] += 1
        if not overlapFlag:
            intermediateClaims.append(claim)
    for claim in intermediateClaims:
        if not claimDoesOverlap(fabric, claim):
            print(claim)

    #print(getOverlapFabricCount(fabric))

if __name__ == "__main__":
    inputs = readfileintowords("input.txt")
    start = time.time()
    part2(inputs)
    end = time.time()
    print(end - start)
