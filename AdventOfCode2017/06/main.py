def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  intInstructions = []
  for i in range(len(lines[0])):
    intInstructions.append(int(lines[0][i]))
  return intInstructions

def part1(inputs):
  previousStates = []
  cycleNum = 0
  currBank = 999
  currBankValue = 0
  while True:
    currBank = getBankIndex(inputs)
    currBankValue = inputs[currBank]
    inputs[currBank] = 0
    for i in range(0,currBankValue):
      inputs[(currBank+i+1)%len(inputs)] += 1
    newState = inputsStr(inputs)
    print newState
    if newState in previousStates:
      return cycleNum+1
    else:
      previousStates.append(newState)
      cycleNum += 1

def getBankIndex(inputs):
  maxim = max(inputs)
  for i in range(len(inputs)):
    if inputs[i] == maxim:
      return i

def inputsStr(inputs):
  newStr = ""
  for i in range(0, len(inputs)):
    newStr += str(inputs[i])
  return newStr

def part2take1(inputs):
  previousStates = []
  cycleNum = 0
  currBank = 999
  currBankValue = 0
  while True:
    currBank = getBankIndex(inputs)
    currBankValue = inputs[currBank]
    inputs[currBank] = 0
    for i in range(0,currBankValue):
      inputs[(currBank+i+1)%len(inputs)] += 1
    newState = inputsStr(inputs)
    if newState in previousStates:
      for i in range(0,10):
        currBank = getBankIndex(inputs)
        currBankValue = inputs[currBank]
        inputs[currBank] = 0
        for i in range(0,currBankValue):
          inputs[(currBank+i+1)%len(inputs)] += 1
        newState = inputsStr(inputs)
        previousStates.append(newState)
      findDuplcates(previousStates)
      return cycleNum+1
    else:
      previousStates.append(newState)
      cycleNum += 1

def part2(inputs):
  previousStates = []
  cycleNum = 0
  currBank = 999
  currBankValue = 0
  while True:
    currBank = getBankIndex(inputs)
    currBankValue = inputs[currBank]
    inputs[currBank] = 0
    for i in range(0,currBankValue):
      inputs[(currBank+i+1)%len(inputs)] += 1
    newState = inputsStr(inputs)
    print newState
    if newState in previousStates:
      val = previousStates.index(newState)
      return len(previousStates)-val
    else:
      previousStates.append(newState)
      cycleNum += 1

def findDuplcates(inputs):
  for i in range(len(inputs)):
    if inputs.count(inputs[i]) > 1:
      print str(i) + ":: " + inputs[i] + ", ",
      if (i+1) < len(inputs):
        print inputs[i+1]
      print ""

if __name__ == "__main__":
  inputs = readfileintowords("input.txt")
  test = [0,2,7,0]
  print part2(inputs)
  #print part1(inputs)
