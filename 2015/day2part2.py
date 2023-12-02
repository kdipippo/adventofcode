# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    for i in range(len(lines)):
        dimensions.append(map(int,lines[i].split('x')))
    return dimensions

def surfaceArea(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l

def smallSide(l,w,h):
    return min(l*w, w*h, h*l)

def totalSurfaceArea(dim):
    totalSA = 0
    for i in range(len(dim)):
        totalSA += surfaceArea(dim[i][0],dim[i][1],dim[i][2]) + smallSide(dim[i][0],dim[i][1],dim[i][2])
    return totalSA

def ribbonCalc(l,w,h):
    return l*w*h + 2*(l+w+h-max(l,w,h))

def totalRibbonCalc(dim):
    totalRibbon = 0
    for i in range(len(dim)):
        totalRibbon += ribbonCalc(dim[i][0],dim[i][1],dim[i][2])
    return totalRibbon

if __name__ == "__main__":
    test1 = [[2,3,4]]
    test2 = [[1,1,10]]

    #print totalSurfaceArea(test1)
    #print totalSurfaceArea(test2)
    print totalRibbonCalc(test1)
    print totalRibbonCalc(test2)

    print totalRibbonCalc(formatInput('input.txt'))
