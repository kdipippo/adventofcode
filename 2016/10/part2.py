# returns contents of a file
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def isTheOne(bots,chip1,chip2):
    chips = bots.values()
    trueChips = []
    trueChips.append(chip1)
    trueChips.append(chip2)
    trueChips = sorted(trueChips)
    trueChips2 = sorted(trueChips,reverse=True)
    if trueChips in chips:
        return bots.keys()[bots.values().index(trueChips)]
    if trueChips2 in chips:
        return bots.keys()[bots.values().index(trueChips2)]
    return '' # False string

def readValue(instructs, bots):
    #value 3 goes to bot 1
    botName = instructs[-2] + instructs[-1].zfill(3)
    if botName not in bots:
        bots[botName] = []
        bots[botName].append(int(instructs[1]))
    elif len(bots[botName]) < 2:
        bots[botName].append(int(instructs[1]))
        bots[botName].sort()

def readDists(instructs, bots):
    #bot 2 gives low to bot 1 and high to bot 0
    giver = instructs[0] + instructs[1].zfill(3)
    if giver not in bots:
        bots[giver] = []
        return False
    elif len(bots[giver]) < 2:
        return False
    else:
        receiver1 = instructs[5] + instructs[6].zfill(3)
        receiver2 = instructs[-2] + instructs[-1].zfill(3)
        if receiver1 not in bots:
            bots[receiver1] = []
        if receiver2 not in bots:
            bots[receiver2] = []
        chips = bots[giver]
        bots[giver] = []
        bots[receiver1].append(min(chips))
        bots[receiver2].append(max(chips))
        return True

def printingBots(bots):
    for bot in sorted(bots.iterkeys()):
        print bot + ":\t",
        for chip in bots[bot]:
            print str(chip) + "\t",
        print ""
    print "----"

def part2(phrase,chip1,chip2):
    bots = {} # key is bot #, value is a 2-value list
    chipDists = [] # new array to keep track of non-value assigning commands
    for i in range(len(phrase)):
        instructs = phrase[i].split(" ")
        if len(instructs) == 6:
            readValue(instructs,bots)
        else:
            chipDists.append(instructs)
    # now proceed with chip distribution
    if isTheOne(bots,chip1,chip2):
        return isTheOne(bots,chip1,chip2)
    #printingBots(bots)
    chipIndex = 0
    while len(chipDists) > 0:
        doneInstruct = readDists(chipDists[chipIndex],bots)
        if doneInstruct: # instruction was able to be completed
            chipDists.remove(chipDists[chipIndex])
        chipIndex += 1
        if len(chipDists) != 0:
            chipIndex = chipIndex % len(chipDists)
        #if isTheOne(bots,chip1,chip2):
            #printingBots(bots)
            #return isTheOne(bots,chip1,chip2)
    printingBots(bots)
    return "???"

# ==================================================
if __name__ == "__main__":
    #43 is too low
    print part2(formatInput('input.txt'),61,17)
    

    
