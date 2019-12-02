# returns contents of a file
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def reverse(chipORgen):
    components = list(chipORgen)
    if components[1] == "G":
        components[1] = "M"
    elif components[1] == "M":
        components[1] = "G"
    return "".join(components)

def readFloors(floorsList):
    floors = {}
    for i in range(len(floorsList)):
        floorName = "F" + str(i+1)
        parts = []
        if i == 0:
            parts.append("E")
        if "hydrogen generator" in floorsList[i]:
            parts.append("HG")
        if "hydrogen-compatible microchip" in floorsList[i]:
            parts.append("HM")
        if "lithium generator" in floorsList[i]:
            parts.append("LG")
        if "lithium-compatible microchip" in floorsList[i]:
            parts.append("LM")
        floors[floorName] = parts
    return floors

def printFloors(floors):
    floorNum = 4
    allParts = ["E","HG","HM","LG","LM"]
    while floorNum > 0:
        floorName = "F" + str(floorNum)
        floorStr = floorName + " "
        for i in range(len(allParts)):
            if allParts[i] in floors[floorName]:
                floorStr += allParts[i] + " "
                if allParts[i] == "E":
                    floorStr += " "
            else:
                floorStr += ".  "
        print floorStr
        floorNum -= 1


# ==================================================
if __name__ == "__main__":
    floors = readFloors(formatInput('testinput.txt'))
    printFloors(floors)

    
