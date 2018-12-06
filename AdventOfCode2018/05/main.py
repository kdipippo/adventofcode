import time

def readfileintowords(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def isLowercase(letter):
    if letter in "abcdefghijklmnopqrstuvwxyz":
        return True
    return False

def isUppercase(letter):
    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    return False

def oneReaction(element):
    hadReaction = False
    newElement = ""
    i = 0
    while i < len(element):
        if i == len(element)-1:
            newElement += element[i]
            i += 1
        elif element[i].lower() == element[i+1].lower() and ((isUppercase(element[i]) and isLowercase(element[i+1])) or (isLowercase(element[i]) and isUppercase(element[i+1]))):
            i += 2
            hadReaction = True
        else:
            newElement += element[i]
            i += 1
    return hadReaction,newElement

def react(element):
    print("#############################")
    hadReaction = True
    newElement = element
    while hadReaction:
        hadReaction,newElement = oneReaction(newElement)
    print(newElement)
    print(len(newElement))

def replaceReact(pairs, element):
    while any(substring in element for substring in pairs):
        for pair in pairs:
            element = element.replace(pair,"")
    return len(element)

def polymerRemoval(element):
    pairs = []
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(lowers)):
        pairs.append(lowers[i]+uppers[i])
        pairs.append(uppers[i]+lowers[i])
    for i in range(len(lowers)):
        newElement = element.replace(lowers[i],"").replace(uppers[i],"")
        print(uppers[i] + "/" + lowers[i] + " - " + str(replaceReact(pairs, newElement)))

if __name__ == "__main__":
    input = readfileintowords("input.txt")[0]
    start = time.time()
    '''
    replaceReact("aA")
    replaceReact("abBA")
    replaceReact("abAB")
    replaceReact("aabAAB")
    '''
    #polymerRemoval("dabAcCaCBAcCcaDA")
    polymerRemoval(input)
    end = time.time()
    print(end - start)
