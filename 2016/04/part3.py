import collections
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

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
    return "-".join(encryptedName),"".join(encryptedName),sectorID,checksum

def checksumValidity(checksum, cipher):
    freqDict = collections.Counter(cipher)
    correctChecksum = [v[0] for v in sorted(freqDict.iteritems(), key=lambda(k, v): (-v, k))]
    correctChecksum = "".join(correctChecksum)
    if checksum == correctChecksum[:5]:
        return True
    return False

def cipherParser(ciphertext):
    dashedCipher,cipher,sectorID,checksum = convertCiphertext(ciphertext)
    if checksumValidity(checksum,cipher):
        plaintext = decryption(dashedCipher,int(sectorID))
        return plaintext
    return " "

def decryption(dashedCipher,sectorID):
    shift = sectorID % 26
    plaintext = ""
    for i in range(len(dashedCipher)):
        if dashedCipher[i] == "-" or dashedCipher[i] == " ":
            plaintext += " "
        elif dashedCipher[i] in ALPHABET:
            currentIndex = ALPHABET.index(dashedCipher[i])
            newIndex = (currentIndex + shift) % 26
            plaintext += ALPHABET[newIndex]
    return plaintext

if __name__ == "__main__":
    #411182 is too high
    ciphers = formatInput('input.txt')

    test1 = 'aaaaa-bbb-z-y-x-123[abyxz]'   # false
    test2 = 'a-b-c-d-e-f-g-h-987[abcde]'   # true
    test3 = 'not-a-real-room-404[oarel]'   # true
    test4 = 'totally-real-room-200[decoy]' # false
    TESTFLAG = False
    
    if TESTFLAG :
        print cipherParser(test1)
        print cipherParser(test2)
        print cipherParser(test3)
        print cipherParser(test4)
        print decryption('qzmt-zixmtkozy-ivhz',343)
    
    rooms = []
    for i in range(len(ciphers)):
        result = cipherParser(ciphers[i])
        if result != " ":
            rooms.append(result)
    rooms.sort()
    for i in range(len(rooms)):
        print rooms[i]
    
