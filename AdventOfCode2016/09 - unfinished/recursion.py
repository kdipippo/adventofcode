# returns contents of a file
def formatInput(filename):
    triangles = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines[0]

def marker(phrase,currIndex):
    markPhrase = ""
    markIndex = currIndex+1
    while phrase[markIndex] != ')':
        markPhrase += phrase[markIndex]
        markIndex += 1
    advance = len(markPhrase) + 2
    markList = markPhrase.split('x')
    return int(markList[0]),int(markList[1]),advance

def recursion(phrase):
    # crop string until the tag is separated from the rest of it
    #X(3x3)XYZ
    recurStr = ""
    index = 0
    while phrase[index] != "(":
        recurStr += phrase[index]
        index += 1

    # (3x3)XYZ
    print "PHRASE:",phrase
    a,b,advance = marker(phrase,index)
    index += advance # XYZ

    if '(' not in phrase[index:index+a]:
        print "STOPPING ON:",phrase[index:index+a]
        newStr = phrase[index:index+a]
        newStr = newStr*b
        return recurStr + newStr
    else:
        print "RECURSION ON:",phrase[index:index+a]
        return recurStr + recursion(phrase[index:index+a])*b

def part2(phrase):
    index = 0
    recurStr = ""
    while index < len(phrase):
        if phrase[index] != '(':
            recurStr += phrase[index]
            index += 1
        else:
            a,b,advance = marker(phrase,index)
            recurStr += recursion(phrase[index:index+a+advance])
            index += advance+a
    return recurStr
        

# ==================================================
if __name__ == "__main__":
    commands = formatInput('input.txt')
    test1 = '(3x3)XYZ(3x3)ABC(3x3)DEF'
    test2 = 'X(8x2)(3x3)ABCY'
    test3 = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    test4 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    test41 = '(3x3)ABC(2x3)XY(5x2)PQRST'
    test42 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRST'

    #print part2(test41)
    print part2(test42)

    
