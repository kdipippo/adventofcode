# returns contents of a file
def formatInput(filename):
    triangles = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def hasABA(IP):
    abas = []
    for i in range(len(IP)-2):
        if IP[i] == IP[i+2] and IP[i] != IP[i+1]:
            aba = IP[i]+IP[i+1]+IP[i+2]
            abas.append(aba)
    actualabas = []
    for i in range(len(abas)):
        aba = abas[i]
        bab = aba[1]+aba[0]+aba[1]
        if bab in abas:
            actualabas.append(aba)
    return actualabas

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

def supportsSSL(IP):
    abas = []
    babs = []
    squareFlag = False
    #aba is outside hyperlink, bab is inside hyperlink
    for i in range(len(IP)-2):
        if IP[i] == '[':
            squareFlag = True
        if IP[i] == IP[i+2] and IP[i] != IP[i+1] and squareFlag:
            bab = IP[i]+IP[i+1]+IP[i+2]
            babs.append(bab)
        if IP[i] == ']':
            squareFlag = False
    if len(babs) == 0:
        return False
    for i in range(len(babs)):
        # flip
        aba = babs[i][1]+babs[i][0]+babs[i][1]
        abas.append(aba)
    for i in range(len(IP)-2):
        if IP[i] == '[':
            squareFlag = True
        if IP[i] == IP[i+2] and IP[i] != IP[i+1] and not squareFlag:
            bab = IP[i]+IP[i+1]+IP[i+2]
            if bab in abas:
                return True
        if IP[i] == ']':
            squareFlag = False
    return False

def supportsSSL_ver1(IP):
    squareFlag = False
    a = ""
    b = ""
    #aba is outside hyperlink, bab is inside hyperlink
    for i in range(len(IP)-2):
        if IP[i] == '[':
            squareFlag = True
        if IP[i] == IP[i+2] and IP[i] != IP[i+1] and squareFlag:
            b = IP[i]
            a = IP[i+1]
        if IP[i] == ']':
            squareFlag = False
    if a == "" or b == "":
        return False
    for i in range(len(IP)-2):
        if IP[i] == '[':
            squareFlag = True
        if IP[i] == IP[i+2] and IP[i] != IP[i+1] and IP[i] == a and IP[i+1] == b and not squareFlag:
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

def part2(inputfile):
    aba_bab = 0
    testing = []
    for i in range(len(inputfile)):
        #print supportsSSL(inputfile[i])
        if supportsSSL(inputfile[i]):
            aba_bab += 1
        elif len(hasABA(inputfile[i])) > 0:
            testing.append(inputfile[i])
            testing.append(hasABA(inputfile[i]))
    return aba_bab, testing

# ==================================================
if __name__ == "__main__":
    # true, false, false, true
    
    test = ['abba[mnop]qrst','abcd[bddb]xyyx','aaaa[qwer]tyui','ioxxoj[asdfgh]zxcvbn']
    test2 = ['aba[bab]xyz','xyx[xyx]xyx','aaa[kek]eke','zazbz[bzb]cdb']
    inputfile = formatInput('input.txt')
    #print part2(test2)
    #152 is too low
    aba,testing = part2(inputfile)
    print aba
    '''
    for i in range(len(testing)):
        print testing[i]
    '''
