# returns contents of a file
def formatInput(filename):
    triangles = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def supportsABBA(IP):
    squareFlag = False
    for i in range(len(IP)-3):
        if IP[i] == '[':
            squareFlag = True
        if IP[i] == IP[i+3] and IP[i+1] == IP[i+2] and IP[i] != IP[i+1] and squareFlag:
            return False
        if IP[i] == ']':
            squareFlag = False
    for i in range(len(IP)-3):
        if IP[i] == '[':
            squareFlag = True
        if IP[i] == IP[i+3] and IP[i+1] == IP[i+2] and IP[i] != IP[i+1] and not squareFlag:
            return True
        if IP[i] == ']':
            squareFlag = False
    return False

def part1(inputfile):
    abba = 0
    for i in range(len(inputfile)):
        if supportsABBA(inputfile[i]):
            abba += 1
    return abba
        

# ==================================================
if __name__ == "__main__":
    # true, false, false, true
    
    test = ['abba[mnop]qrst','abcd[bddb]xyyx','aaaa[qwer]tyui','ioxxoj[asdfgh]zxcvbn']
    inputfile = formatInput('input.txt')
    print part1(inputfile)
    
    
