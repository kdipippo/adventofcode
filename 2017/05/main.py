def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  intInstructions = []
  for i in range(len(lines)):
    intInstructions.append(int(lines[i][0]))
  return intInstructions

def part1(inputs):
  currIndex = 0
  numInputs = len(inputs)
  counter = 0
  while currIndex >= 0 and currIndex < numInputs:
    tempIndex = currIndex
    currIndex += inputs[tempIndex]
    inputs[tempIndex] += 1
    counter += 1
  print inputs
  return counter

def part2(inputs):
  currIndex = 0
  numInputs = len(inputs)
  counter = 0
  while currIndex >= 0 and currIndex < numInputs:
    tempIndex = currIndex
    currIndex += inputs[tempIndex]
    if inputs[tempIndex] >= 3:
      inputs[tempIndex] -= 1
    else:
      inputs[tempIndex] += 1
    counter += 1
  print inputs
  return counter

if __name__ == "__main__":
  inputs = readfileintowords("input.txt")
  test = [0,3,0,1,-3]
  print part2(inputs)
  #print part1(inputs)
