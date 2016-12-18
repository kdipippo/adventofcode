import hashlib

# returns 'c',True if character exists three in a row, i.e. 'ccc'
# returns '',False if not the case
def containsThree(teststring):
    for i in range(len(teststring)-2):
        if teststring[i] == teststring[i+1] and teststring[i] == teststring[i+2]:
            return teststring[i],True
    return '',False

def validThousandHashes(char3,thousandList):
    five = char3*5
    for i in range(len(thousandList)):
        if five in thousandList[i]:
            return True
    return False

def calcHash(salt):
    allHashes = []
    validHashes = []
    saltIndex = 0
    # starting off initially
    for i in range(1001):
        allHashes.append(hashlib.md5(salt + str(i)).hexdigest())
    while len(validHashes) < 64:
        # contains3 on allHashes[saltIndex]
        char3,bool3 = containsThree(allHashes[saltIndex])
        if bool3: # passes containsThree
            # valid1000 on allHashes[saltIndex+1:]
            if validThousandHashes(char3,allHashes[saltIndex+1:]):
                validHashes.append(saltIndex)
        allHashes.append(hashlib.md5(salt + str(saltIndex+1001)).hexdigest())
        saltIndex += 1
    return validHashes

if __name__ == "__main__":
    salt1 = 'abc'
    salt2 = 'jlmsuwbz'

    print calcHash(salt2)

    
