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

def decompress(phrase):
    currIndex = 0
    dPhrase = ""
    while currIndex < len(phrase):
        if phrase[currIndex] == '(':
            a,b,advance = marker(phrase,currIndex)
            currIndex += advance
            for i in range(b):
                dPhrase += phrase[currIndex:currIndex+a]
            currIndex += a
        else:
            dPhrase += phrase[currIndex]
            currIndex += 1
    return len(dPhrase)

# This needs to use recursion if it wants to look pretty
def decompress_ver2(phrase):
    currIndex = 0
    dPhraseLength = 0
    while currIndex < len(phrase):
        if phrase[currIndex] == '(':
            a,b,advance = marker(phrase,currIndex)
            currIndex += advance
            for i in range(b):
                dPhraseLength += a
            currIndex += a
        else:
            dPhraseLength += 1
            currIndex += 1
    return dPhraseLength
    

# ==================================================
if __name__ == "__main__":
    commands = formatInput('input.txt')
    test1 = '(8x10)SBTLHXZP'
    tests = ['ADVENT', # ADVENT
             'A(1x5)BC', # ABBBBBC
             '(3x3)XYZ', # XYZXYZXYZ
             'A(2x2)BCD(2x2)EFG', # ABCBCDEFEFG
             '(6x1)(1x3)A', # (1x3)A
             'X(8x2)(3x3)ABCY'] # X(3x3)ABC(3x3)ABCY
    
    for i in range(len(tests)):
        print decompress(tests[i])
    
    #183292 is too high
    #print decompress(commands)
    

    
