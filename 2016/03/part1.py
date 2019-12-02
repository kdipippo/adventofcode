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
    print triangleTally(triangles)
    '''
    test1 = [3,4,5]
    test2 = [7,10,5]
    test3 = [5,10,25]

    print isTriangle(test1)
    print isTriangle(test2)
    print isTriangle(test3)
    '''
