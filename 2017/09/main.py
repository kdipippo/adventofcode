def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines[0][0]

def part1(stream):
  stream = removeExclamations(stream)
  #print stream
  stream = removeGarbage(stream)
  stream = stream.replace(",","")
  return bracesScore(stream)

def part2(stream):
  stream = removeExclamations(stream)
  charNum = removeGarbage_withChars(stream)
  return charNum

def removeExclamations(stream):
  newStream = ""
  currentIndex = 0
  while currentIndex < len(stream):
    if stream[currentIndex] == "!":
      currentIndex += 2
    else:
      newStream += stream[currentIndex]
      currentIndex += 1
  return newStream

def removeGarbage(stream):
  newStream = ""
  currentIndex = 0
  garbageFlag = False
  while currentIndex < len(stream):
    if garbageFlag and stream[currentIndex] == ">":
      garbageFlag = False
    elif not garbageFlag and stream[currentIndex] == "<":
      garbageFlag = True
    elif not garbageFlag and stream[currentIndex] != "<":
      newStream += stream[currentIndex]
    currentIndex += 1
  return newStream

def removeGarbage_withChars(stream):
  newStream = ""
  currentIndex = 0
  garbageFlag = False
  charNum = 0
  while currentIndex < len(stream):
    if garbageFlag and stream[currentIndex] == ">":
      garbageFlag = False
    elif garbageFlag and stream[currentIndex] != ">":
      charNum += 1
    elif not garbageFlag and stream[currentIndex] == "<":
      garbageFlag = True
    elif not garbageFlag and stream[currentIndex] != "<":
      newStream += stream[currentIndex]
    currentIndex += 1
  return charNum

def bracesScore(stream):
  depth = 0
  score = 0
  for i in range(len(stream)):
    if stream[i] == "{":
      depth += 1
    elif stream[i] == "}":
      score += depth
      depth -= 1
  return score

if __name__ == "__main__":
  stream = readfileintowords("input.txt")

  #test1 = "{}"
  #test2 = "{{{}}}"
  #test3 = "{{}{}}"
  #test4 = "{{{}{}{{}}}}"
  #print bracesScore(test1)
  #print bracesScore(test2)
  #print bracesScore(test3)
  #print bracesScore(test4)
  #print part1(stream)

  test1 = "<>"
  test2 = "<random characters>"
  test3 = "<<<<>"
  test4 = "<{!>}>"
  test5 = "<!!>"
  test6 = "<!!!>>"
  test7 = '<{o"i!a,<{i<a>'
  print part2(test1)
  print part2(test2)
  print part2(test3)
  print part2(test4)
  print part2(test5)
  print part2(test6)
  print part2(test7)
  print part2(stream)
  
