import hashlib

VALIDDOORS = 'bcdef'
DIRECTIONS = 'UDLR'

def returnHash(hashStr):
    return hashlib.md5(hashStr).hexdigest()

def bitwiseAdd(bit1,bit2):
    # making my own version that preserves the binary output
    retBit = ''
    for i in range(len(bit1)):
        if bit1[i] == bit2[i]:
            retBit += '1'
        else:
            retBit += '0'
    return retBit

def openDoors(salt,pathTaken):
    udlr = returnHash(salt + pathTaken)[:4]
    udlrFlags = ''
    for i in range(len(udlr)):
        if udlr[i] in VALIDDOORS:
            udlrFlags += '1'
        else:
            udlrFlags += '0'
    return udlrFlags

def moveLocation(currentLoc, direc):
    if direc == 0:
        currentLoc[0] -= 1
    elif direc == 1:
        currentLoc[0] += 1
    elif direc == 2:
        currentLoc[1] -= 1
    elif direc == 3:
        currentLoc[1] += 1
    return currentLoc    

def validLocation(currentLoc):
    # hard codes the fact that the grid is from 0-3 both directions
    udlrFlags = ['1']*4 # start valid and close off
    if currentLoc[0] == 0: # close Up
        udlrFlags[0] = '0'
    if currentLoc[0] == 3: # close Down
        udlrFlags[1] = '0'
    if currentLoc[1] == 0: # close Left
        udlrFlags[2] = '0'
    if currentLoc[1] == 3: # close Right
        udlrFlags[3] = '0'
    return "".join(udlrFlags)        

def moving(salt,pathTaken,currentLoc):
    udlrDoors = openDoors(salt,pathTaken)
    udlrLoc = validLocation(currentLoc)
    # bitwise addition for valid doors
    choices = bitwiseAdd(udlrDoors,udlrLoc)
    print choices
    '''
    if choices.count('1') > 0:
        for i in range(len(choices)):
            if choices[i] == '1':
                pathTaken += DIRECTIONS[i]
                currentLoc = moveLocation(currentLoc, i)
                if currentLoc == [3,3]:
                    pathTaken += '!'
                    print pathTaken
                else:
                    moving(salt,pathTaken,currentLoc)
    '''

def part1(salt):
    pathTaken = ""
    currentLoc = [0,0]
    moving(salt,pathTaken,currentLoc)

    pathTaken += 'D'
    currentLoc = moveLocation(currentLoc,1)
    moving(salt,pathTaken,currentLoc)

    pathTaken += 'U'
    currentLoc = moveLocation(currentLoc,0)
    moving(salt,pathTaken,currentLoc)

    pathTaken += 'R'
    currentLoc = moveLocation(currentLoc,3)
    moving(salt,pathTaken,currentLoc)

    pathTaken += 'U'
    currentLoc = moveLocation(currentLoc,0)
    moving(salt,pathTaken,currentLoc)

    pathTaken += 'R'
    currentLoc = moveLocation(currentLoc,3)
    moving(salt,pathTaken,currentLoc)

if __name__ == "__main__":
    salt1 = 'hijkl'
    salt2 = 'ihgpwlah'
    salt3 = 'kglvqrro'
    salt4 = 'ulqzkmiv'
    salt5 = 'mmsxrhfx'

    part1(salt1)

    
