def getSpace(x,y,faveNum):
    num = (x*x) + (3*x) + (2*x*y) + y + (y*y) + faveNum
    binary = bin(num)[2:]
    oneCount = binary.count('1')
    if oneCount % 2 == 0:
        return '.'
    return '#'

# used to visualize the grid
def generateGrid(faveNum, width, height):
    grid = []
    for i in range(height):
        grid.append(['-']*width)

    # rewritten to keep x and y consistent
    for y in range(height):
        for x in range(width):
            grid[y][x] = getSpace(x,y,faveNum)
    return grid

# used to visualize the smaller grid
def printGrid(grid):
    #print "  0123456789"
    for i in range(len(grid)):
        print "".join(grid[i])


def search(gx,gy,x,y,faveNum,grid):
    grid[y][x] = 'O'
    # returns True if it has found end of maze
    if x == gx and y == gy:
        return True
    # returns False if it encounters a wall
    elif getSpace(x,y,faveNum) == '#':
        return False

    # recursive search        
    if    ((search(gx,gy,x+1,y,  faveNum,grid))
        or (search(gx,gy,x,  y-1,faveNum,grid))
        or (search(gx,gy,x-1,y,  faveNum,grid))
        or (search(gx,gy,x,  y+1,faveNum,grid))):
        return True
    return False

def part1(goalx,goaly,width,height,faveNum):
    x = 1
    y = 1
    grid = generateGrid(faveNum, width, height)
    grid[goaly][goalx] = 'G'
    search(goalx,goaly,x,y,faveNum,grid)
    printGrid(grid)

if __name__ == "__main__":
    printGrid(generateGrid(10, 10, 7))
    #printGrid(generateGrid(1358, 40, 40))
    #part1(7,4,10,7,10)
