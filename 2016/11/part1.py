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
        if "curium generator" in floorsList[i]:
            parts.append("CG")
        if "curium-compatible microchip" in floorsList[i]:
            parts.append("CM")
        if "plutonium generator" in floorsList[i]:
            parts.append("PG")
        if "plutonium-compatible microchip" in floorsList[i]:
            parts.append("PM")
        if "ruthenium generator" in floorsList[i]:
            parts.append("RG")
        if "ruthenium-compatible microchip" in floorsList[i]:
            parts.append("RM")
        if "strontium generator" in floorsList[i]:
            parts.append("SG")
        if "strontium-compatible microchip" in floorsList[i]:
            parts.append("SM")
        if "thulium generator" in floorsList[i]:
            parts.append("TG")
        if "thulium-compatible microchip" in floorsList[i]:
            parts.append("TM")
        floors[floorName] = parts
    return floors

def printFloors(floors):
    floorNum = 4
    allParts = ["E","CG","CM","PG","PM","RG","RM","SG","SM","TG","TM"]
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
    floors = readFloors(formatInput('input.txt'))
    printFloors(floors)

    
