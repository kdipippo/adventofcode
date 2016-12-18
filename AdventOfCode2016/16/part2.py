def calcDragon(a):
    b = a[::-1]
    b = b.replace('0','a').replace('1','0').replace('a','1')
    finalStr = a + '0' + b
    return finalStr

def calcChecksum(inputStr):
    index = 0
    a = inputStr
    b = ''
    checksumflag = True
    while checksumflag: #exit when checksum is odd length
        while index < len(a):
            if a[index] == a[index+1]:
                b += '1'
            else:
                b += '0'
            index += 2
        if len(b) % 2 == 0:
            a = b
            b = ''
            index = 0
        else:
            return b

def part1(length, initState):
    mState = initState #modifiedState
    while len(mState) < length:
        mState = calcDragon(mState)
    mState = mState[:length]
    return calcChecksum(mState)

if __name__ == "__main__":
    print part1(20,'10000')
    print part1(272,'11100010111110100')
    print part1(35651584,'11100010111110100')
