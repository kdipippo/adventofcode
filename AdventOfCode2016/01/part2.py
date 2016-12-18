DEBUG_FLAG = False
FIRST_DUPLICATE = ""

# takes in a file name
# returns a list of strings of form 'R#' or 'L#'
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines[0].split(', ')

# takes in a list of strings of form R# or L#
# returns a 2D list where inner list is of the form ['R/L', #]
def parseInput(coordList):
    returnList = []
    for i in range(0,len(coordList)):
        coord = []
        coord.append(coordList[i][0]) #direction
        coord.append(int(coordList[i][1:])) #distance
        returnList.append(coord)
    return returnList

# takes in two integers
# returns as a 1-dimensional list
def makeLocation(x, y):
    #location = [x,y]
    location = str(x) + "," + str(y)
    return location

def duplicateFlagger(pastLoc, newLoc):
    global FIRST_DUPLICATE
    if newLoc in pastLoc:
        if DEBUG_FLAG:
            print "DUPLICATE FOUND at",newLoc
        if FIRST_DUPLICATE == "":
            FIRST_DUPLICATE = newLoc

# takes in currentDirection and futureDirection
# returns changed currentDirection
def move(pastLocations, cd, fd, currentLocation, distance):
    # cd = currentDirection; fd = futureDirection
    # right R or left L = down        
    if (cd == "right" and fd == "R") or (cd == "left" and fd == "L"):
        for i in range(1,distance+1):
            newLocation = makeLocation(currentLocation[0],currentLocation[1]-i)
            if DEBUG_FLAG:
                print newLocation
            duplicateFlagger(pastLocations, newLocation)
            pastLocations.append(newLocation)
        currentLocation[1] -= distance
        return "down"
    # right L or left R = up
    elif (cd == "right" and fd == "L") or (cd == "left" and fd == "R"):
        for i in range(1,distance+1):
            newLocation = makeLocation(currentLocation[0],currentLocation[1]+i)
            if DEBUG_FLAG:
                print newLocation
            duplicateFlagger(pastLocations, newLocation)
            pastLocations.append(newLocation)
        currentLocation[1] += distance
        return "up"
    # down R or up L = left
    # includes special case for starting input
    elif (cd == "" and fd == "L") or (cd == "down" and fd == "R") or (cd == "up" and fd == "L"):
        for i in range(1,distance+1):
            newLocation = makeLocation(currentLocation[0]-i,currentLocation[1])
            if DEBUG_FLAG:
                print newLocation
            duplicateFlagger(pastLocations, newLocation)
            pastLocations.append(newLocation)
        currentLocation[0] -= distance
        return "left"
    # down L or up R = right
    # includes special case for starting input
    elif (cd == "" and fd == "R") or (cd == "down" and fd == "L") or (cd == "up" and fd == "R"):
        for i in range(1,distance+1):
            newLocation = makeLocation(currentLocation[0]+i,currentLocation[1])
            if DEBUG_FLAG:
                print newLocation
            duplicateFlagger(pastLocations, newLocation)
            pastLocations.append(newLocation)
        currentLocation[0] += distance
        return "right"

def computeDist(coordList):
    global FIRST_DUPLICATE
    pastLocations = []
    currentLocation = [0,0] # starting at origin
    currentDirection = ""
    for i in range(0,len(coordList)):
        currentDirection = move(pastLocations,currentDirection,coordList[i][0],currentLocation,int(coordList[i][1]))
        #print "Car moves",currentDirection
    solution = FIRST_DUPLICATE
    FIRST_DUPLICATE = ""
    return solution
    

# =============================================================
if __name__ == "__main__":
    '''
    test1 = ['R2','L3'] #return 5 blocks away
    test2 = ['R2','R2','R2'] #returns 2 blocks away
    test3 = ['R5','L5','R5','R3'] #returns 12 blocks away

    print computeDist(test1)
    print computeDist(test2)
    print computeDist(test3)
    '''
    print computeDist(parseInput(formatInput('input.txt')))

    
    test4 = ['R8','R4','R4','R8']
    test5 = ['R5','L2','L3','R2','R2','R6']
    print computeDist(test4)
    print computeDist(test5)
    
    
    
