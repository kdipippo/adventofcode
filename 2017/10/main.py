from array import array

def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  finalStr = lines[0][0].split(",")
  for i in range(len(finalStr)):
    finalStr[i] = int(finalStr[i])
  return finalStr

def readfileintostr(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines[0][0]

def part1(stream):
  print knot(stream)

def knot(lengths):
  klist = []
  for i in range(0, 256):
    klist.append(i)
  #testlist = [0,1,2,3,4]
  kcurrPos = 0
  kskipSize = 0
  for i in range(len(lengths)):
    sublist = []
    for j in range(kcurrPos,kcurrPos+lengths[i]):
      sublist.append(klist[j%len(klist)])
    sublist.reverse()
    sublistCount = 0
    for j in range(kcurrPos,kcurrPos+lengths[i]):
      klist[j%len(klist)] = sublist[sublistCount]
      sublistCount += 1
    kcurrPos += lengths[i] + kskipSize
    kcurrPos %= len(klist)
    kskipSize += 1
  return klist

def part2(inputStr):
  print "==========inputStr=========="
  print inputStr
  stream = convertstrtobytearray(inputStr)
  print "==========stream=========="
  print stream
  kcurrPos = 0
  kskipSize = 0
  klist = []
  for i in range(0, 256):
    klist.append(i)
  for i in range(0,64):
    klist,kcurrPos,kskipSize = knotHashRound(stream,klist,kcurrPos,kskipSize)
  sparseHash = list(klist)
  print "==========sparseHash=========="
  print sparseHash
  denseHash = sparseToDense(sparseHash)
  print "==========denseHash=========="
  print denseHash
  print "==========hex=========="
  return denseToHex(denseHash)

def convertstrtobytearray(inputStr):
  bytes = array("B",inputStr)
  finalBytes = []
  for i in range(len(bytes)):
    finalBytes.append(bytes[i])
  suffixBytes = [17, 31, 73, 47, 23]
  for i in range(len(suffixBytes)):
    finalBytes.append(suffixBytes[i])
  return finalBytes

def knotHashRound(lengths,klist,kcurrPos,kskipSize):
  for i in range(len(lengths)):
    sublist = []
    for j in range(kcurrPos,kcurrPos+lengths[i]):
      sublist.append(klist[j%len(klist)])
    sublist.reverse()
    sublistCount = 0
    for j in range(kcurrPos,kcurrPos+lengths[i]):
      klist[j%len(klist)] = sublist[sublistCount]
      sublistCount += 1
    kcurrPos += lengths[i] + kskipSize
    kcurrPos %= len(klist)
    kskipSize += 1
  return klist,kcurrPos,kskipSize

def sparseToDense(sparseHash):
  denseHash = []
  for i in range(0,16):
    denseVal = sparseHash[16*i]
    for j in range(1,16):
      denseVal ^= sparseHash[16*i + j]
    denseHash.append(denseVal)
  return denseHash

def denseToHex(denseHash):
  hexStr = ""
  for i in range(len(denseHash)):
    temp = str(hex(denseHash[i]))[2:]
    if len(temp) == 1:
      temp = "0" + temp
    hexStr += temp
  return hexStr

if __name__ == "__main__":
  #stream = readfileintowords("input.txt")
  #test = readfileintowords("test.txt")
  #part1(stream)
  #inputStr = readfileintostr("input.txt")
  print part2("")
  print part2("AoC 2017")
  print part2("1,2,3")
  print part2("1,2,4")
  #35b028fe2c958793f7d5a61d7a08c8
  print part2("197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63")
  
