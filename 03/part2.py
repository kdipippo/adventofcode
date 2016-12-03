# takes in a file name
# returns a list of strings of form 'R#' or 'L#'
def formatInput(filename):
    triangles = []
    with open(filename) as f:
        lines = f.read().splitlines()
    # there's gotta be a way to not use two loops for this
    for i in range(len(lines)):
        triangles.append(map(int,lines[i].split()))
    return triangles

def modifyTriangles(tri):
    newTriangles = []
    i = 0
    while i < len(tri):
        newTriangles.append([tri[i][0],tri[i+1][0],tri[i+2][0]])
        newTriangles.append([tri[i][1],tri[i+1][1],tri[i+2][1]])
        newTriangles.append([tri[i][2],tri[i+1][2],tri[i+2][2]])
        i += 3
    return newTriangles

def isTriangle(points):
    if (sum(points) - max(points)) > max(points):
        return True
    return False

def triangleTally(triangles):
    triangleCount = 0
    for i in range(len(triangles)):
        if isTriangle(triangles[i]):
            triangleCount += 1
    return triangleCount
# ==================================================
if __name__ == "__main__":
    triangles = formatInput('input.txt')
    newTriangles = modifyTriangles(triangles)
    print "triangles =",triangleTally(triangles)
    print "newtriang =",triangleTally(newTriangles)
    
    '''
    test1 = [3,4,5]
    test2 = [7,10,5]
    test3 = [5,10,25]

    print isTriangle(test1)
    print isTriangle(test2)
    print isTriangle(test3)
    '''
