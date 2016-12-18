# takes in a file name
# returns a long string of parentheticals
def formatInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines[0]

def returnFloor(parenthesesString):
    leftCount = parenthesesString.count('(')
    rightCount = parenthesesString.count(')')
    return leftCount-rightCount

if __name__ == "__main__":
    test1 = '(())' #0
    test2 = '(()(()(' #3
    test3 = '))(((((' #3
    print returnFloor(test1)
    print returnFloor(test2)
    print returnFloor(test3)
    
    print returnFloor(formatInput('input.txt'))
