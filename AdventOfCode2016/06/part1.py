import collections

# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    grid = []
    for i in range(len(lines)):
        grid.append(list(lines[i]))
    return grid

def rotate(lis):
    newList = []
    for x in zip(*lis):
        newList2 = []
        for y in x:
            newList2.append(y)
        newList.append(newList2)
    return newList

def rotateAndCalc(lis):
    newList = []
    for x in zip(*lis):
        newList2 = []
        for y in x:
            newList2.append(y)
        word = "".join(newList2)
        newList.append(collections.Counter(word).most_common(1)[0][0])
    return "".join(newList)

if __name__ == "__main__":
    letters = formatInput('testinput.txt')
    letters2 = formatInput('input.txt')
    print rotateAndCalc(letters2)
