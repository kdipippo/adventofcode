import re

# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

if __name__ == "__main__":
    inputFile = formatInput('input.txt')
    filename='test.txt'
    f = open(filename,'w')
    for i in range(len(inputFile)):
        f.write(inputFile[i])
        f.write("\n")
    '''
    with open(filename,'r') as f:
        pat = f.readline()
        print(pat)
        # \"Hello,\s\"\s*\+\s*\"world!\"
        print(repr(pat))
        # '\\"Hello,\\s\\"\\s*\\+\\s*\\"world!\\"'
        assert re.search(pat,'  "Hello, " +   "world!"')  # Shows match was found
    '''       
