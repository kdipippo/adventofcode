# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines[0]

def testOutputHouse(HOUSES):
    for i in range(len(HOUSES)):
        for j in range(len(HOUSES[i])):
            print HOUSES[i][j],
        print ""

def santaMoves(x,y,direc):
    if direc == "^":
        y += 1
    elif direc == "v":
        y -= 1
    elif direc == ">":
        x += 1
    elif direc == "<":
        x -= 1
    return x,y

def presentCounter(houseGrid,directions):
    # initialize starting point
    x = 5
    y = 5
    
    for i in range(len(directions)):
        houseGrid[x][y] += 1
        x,y = santaMoves(x,y,directions[i])
    houseGrid[x][y] += 1
    return houseGrid

def calcHouses(houseGrid):
    totalHouses = 0
    for i in range(len(houseGrid)):
        for j in range(len(houseGrid[i])):
            if houseGrid[i][j] >= 1:
                totalHouses += 1
    return totalHouses

if __name__ == "__main__":
    # even though presents are delivered on an infinite 2D grid,
    #  I will assume simulation can take place in a grid of 1000x1000
    HOUSES = []
    for i in range(1000):
        HOUSES.append([0]*1000)

    directions = formatInput('input.txt')
    #directions = '<><><><><>'
    
    print calcHouses(presentCounter(HOUSES,directions))
    #testOutputHouse(HOUSES)
