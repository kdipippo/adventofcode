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

def presentCounter(startingx, startingy, houseGrid,directions):
    # initialize starting point
    santax = startingx
    santay = startingy
    robox = startingx
    roboy = startingy
    
    houseGrid[santax][santay] += 1
    for i in range(len(directions)):
        if i % 2 == 0: # Santa moves on even
            santax,santay = santaMoves(santax,santay,directions[i])
            houseGrid[santax][santay] += 1
        elif i % 2 == 1: # Robot moves on odd
            robox,roboy = santaMoves(robox,roboy,directions[i])
            houseGrid[robox][roboy] += 1
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
    size = 1000
    for i in range(size):
        HOUSES.append([0]*size)

    directions = formatInput('input.txt')
    #directions = '<><><><><>'
    
    print calcHouses(presentCounter(size/2,size/2,HOUSES,directions))
    #testOutputHouse(presentCounter(size/2,size/2,HOUSES,directions))
