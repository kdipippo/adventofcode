VOWELS = 'aeiou'

# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def spliceString(inputStr,smallIndex):
    startNewStr = inputStr[:smallIndex]
    endNewStr = inputStr[smallIndex+2:]
    return startNewStr,endNewStr

# contains a pair of letter pair that appears twice
def pairFlag(inputStr):
    for i in range(len(inputStr)-1):
        testingStr = inputStr[i] + inputStr[i+1]
        startStr,endStr = spliceString(inputStr,i)
        if testingStr in startStr or testingStr in endStr:
            return True
    return False

# contains letter which repeats with letter two indices away
def abaFlag(inputStr):
    for i in range(len(inputStr)-2):
        if inputStr[i] == inputStr[i+2]:
            return True
    return False

def naughtyOrNice(inputStr):
    if pairFlag(inputStr) and abaFlag(inputStr):
        return True
    return False

if __name__ == "__main__":
    '''
    test1 = 'ugknbfddgicrmopn' # nice
    test2 = 'aaa'              # nice
    test3 = 'jchzalrnumimnmhp' # naughty
    test4 = 'dvszwmarrgswjxmb' # naughty
    '''

    tests = ['qjhvhtzxzqqjkmpb', # true
             'xxyxx',            # true
             'uurcxstgmygtbstg', # false
             'ieodomkazucvgmuy', # false
             'rbadoommlmrictte',] # ?? true
    '''
    for i in range(len(tests)):
        print tests[i],pairFlag(tests[i]),abaFlag(tests[i])
    '''
    
    # 58 is too high
    inputs = formatInput('input.txt')
    niceCount = 0
    for i in range(len(inputs)):
        if naughtyOrNice(inputs[i]):
            niceCount += 1
            #print inputs[i]
    print niceCount
    
    
