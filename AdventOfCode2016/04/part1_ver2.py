import collections

# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def convertCiphertext(ciphertext):
    cipherstring = ciphertext.split('[')
    checksum = cipherstring[1].replace("]","")
    encryptedName = cipherstring[0].split('-') # contains name and ID
    sectorID = encryptedName[-1]
    encryptedName.pop() # remove sectorID
    #print "".join(encryptedName)
    #print "-".join(encryptedName)
    return "".join(encryptedName),sectorID,checksum

def checksumValidity(checksum, cipher):
    freqDict = collections.Counter(cipher)
    correctChecksum = [v[0] for v in sorted(freqDict.iteritems(), key=lambda(k, v): (-v, k))]
    correctChecksum = "".join(correctChecksum)
    if checksum == correctChecksum[:5]:
        return True
    return False

def cipherParser(ciphertext):
    cipher,sectorID,checksum = convertCiphertext(ciphertext)
    if checksumValidity(checksum,cipher):
        return int(sectorID)
    return 0

if __name__ == "__main__":
    #411182 is too high
    ciphers = formatInput('input.txt')

    test1 = 'aaaaa-bbb-z-y-x-123[abyxz]'   # false
    test2 = 'a-b-c-d-e-f-g-h-987[abcde]'   # true
    test3 = 'not-a-real-room-404[oarel]'   # true
    test4 = 'totally-real-room-200[decoy]' # false
    
    print cipherParser(test1)
    print cipherParser(test2)
    print cipherParser(test3)
    print cipherParser(test4)
    
    '''
    totalSectorIDs = 0
    for i in range(len(ciphers)):
        totalSectorIDs += cipherParser(ciphers[i])
    print totalSectorIDs
    '''
