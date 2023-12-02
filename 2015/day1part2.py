# takes in a file name
# returns a long string of parentheticals
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines[0]

def returnBasementIndex(parenthesesString):
    currentFloor = 0
    for i in range(len(parenthesesString)):
        if parenthesesString[i] == '(':
            currentFloor += 1
        elif parenthesesString[i] == ')':
            currentFloor -= 1
        if currentFloor == -1:
            return i+1
    return -1 # if basement is never entered

if __name__ == "__main__":
    test1 = ')' #1
    test2 = '()())' #5
    
    print returnBasementIndex(test1)
    print returnBasementIndex(test2)
    
    print returnBasementIndex(formatInput('input.txt'))
