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
        newList.append(collections.Counter(word).most_common()[-1][0])
    return "".join(newList)

if __name__ == "__main__":
    letters = formatInput('testinput.txt')
    letters2 = formatInput('input.txt')
    print rotateAndCalc(letters2)

    sampleInput = [('g', 23), ('a', 22), ('c', 22), ('b', 22), ('e', 22), ('d', 22), ('f', 22), ('i', 22), ('h', 22), ('k', 22), ('m', 22), ('l', 22), ('o', 22), ('n', 22), ('q', 22), ('p', 22), ('s', 22), ('r', 22), ('u', 22), ('t', 22), ('w', 22), ('v', 22), ('y', 22), ('x', 22), ('z', 22), ('j', 21)]
    #print leastCommon(sampleInput)
