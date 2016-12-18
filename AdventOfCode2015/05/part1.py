VOWELS = 'aeiou'

# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def naughtyOrNice(inputStr):
    # contains at least 3 vowels, aeiou
    vowelCount = 0
    for i in range(len(VOWELS)):
        vowelCount += inputStr.count(VOWELS[i])
    # at least 1 letter twice in a row
    # does not contain 'ab','cd','pq','xy'
    doNotContain = ['ab','cd','pq','xy']
    doubleFlag = False
    dncFlag = True # flip this to indicate wrong
    for i in range(len(inputStr)-1):
        if inputStr[i] == inputStr[i+1]:
            doubleFlag = True
        testingStr = inputStr[i] + inputStr[i+1]
        if testingStr in doNotContain:
            dncFlag = False
    if vowelCount >= 3 and doubleFlag and dncFlag:
        return True
    return False

if __name__ == "__main__":
    test1 = 'ugknbfddgicrmopn' # nice
    test2 = 'aaa'              # nice
    test3 = 'jchzalrnumimnmhp' # naughty
    test4 = 'dvszwmarrgswjxmb' # naughty
    DEBUG_FLAG = False
    if DEBUG_FLAG:
        print naughtyOrNice(test1)
        print naughtyOrNice(test2)
        print naughtyOrNice(test3)
        print naughtyOrNice(test4)

    inputs = formatInput('input.txt')
    niceCount = 0
    for i in range(len(inputs)):
        if naughtyOrNice(inputs[i]):
            niceCount += 1
    print niceCount
