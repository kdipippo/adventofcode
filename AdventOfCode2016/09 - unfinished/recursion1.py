# returns contents of a file
def formatInput(filename):
    triangles = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines[0]

def marker(phrase,index):
    markPhrase = ""
    while phrase[index] != ')':
        markPhrase += phrase[index]
        index += 1
    advance = len(markPhrase) + 2
    markList = markPhrase.split('x')
    return int(markList[0]),int(markList[1]),index
        
def recursionString(data):
    index = 0
    total = ""
    while index < len(data):
        if data[index] == '(':
            index += 1
            length,amount,index = marker(data,index)
            total += amount*recursionString(data[index+1:index+length+1])
            index += length
        else:
            total += data[index]
        index += 1
    return total

def recursionLength(data):
    index = 0
    total = 0
    while index < len(data):
        if data[index] == '(':
            index += 1
            length,amount,index = marker(data,index)
            total += amount*recursionLength(data[index+1:index+length+1])
            index += length
        else:
            total += 1
        index += 1
    return total

def part2(data):
    print recursionLength(data)
    #print recursionString(data)

# ==================================================
if __name__ == "__main__":
    commands = formatInput('input.txt')
    test1 = '(3x3)XYZ(3x3)ABC(3x3)DEF'
    test2 = 'X(8x2)(3x3)ABCY'
    test3 = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    test4 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    test41 = '(3x3)ABC(2x3)XY(5x2)PQRST'
    test42 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX'

    #print part2(test41)
    #part2(test42)
    part2(commands)

    
