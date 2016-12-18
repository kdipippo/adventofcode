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

    return "".join(encryptedName),sectorID,checksum

def checksumValidity(checksum, cipher):
    # find counts for each letter in checksum
    checksumList = []
    for i in range(len(checksum)):
        checksumList.append(cipher.count(checksum[i]))
    # check values are in descending order
    if not all(earlier >= later for earlier, later in zip(checksumList, checksumList[1:])):
        return False
    # check ties
    for i in range(len(checksumList)-1):
        if checksumList[i] == checksumList[i+1]:
            if ALPHABET.index(checksum[i]) > ALPHABET.index(checksum[i+1]):
                return False
    return True

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

    totalSectorIDs = 0
    for i in range(len(ciphers)):
        totalSectorIDs += cipherParser(ciphers[i])
    print totalSectorIDs
