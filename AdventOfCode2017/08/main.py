def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines

def part1(inputs):
  registers = {}
  maxim = 0
  for i in range(len(inputs)):
    destRegisterName = inputs[i][0]
    incOrDec = inputs[i][1]
    destValue = int(inputs[i][2])
    compRegisterName = inputs[i][4]
    compAction = inputs[i][5]
    compValue = int(inputs[i][6])

    if destRegisterName not in registers:
      registers[destRegisterName] = 0
    if compRegisterName not in registers:
      registers[compRegisterName] = 0
    if compAction == '<' and registers[compRegisterName] < compValue:
      registers,maxim = modifyRegister(maxim,incOrDec,registers,destRegisterName,destValue)
    elif compAction == '>' and registers[compRegisterName] > compValue:
      registers,maxim = modifyRegister(maxim,incOrDec,registers,destRegisterName,destValue)
    elif compAction == '<=' and registers[compRegisterName] <= compValue:
      registers,maxim = modifyRegister(maxim,incOrDec,registers,destRegisterName,destValue)
    elif compAction == '>=' and registers[compRegisterName] >= compValue:
      registers,maxim = modifyRegister(maxim,incOrDec,registers,destRegisterName,destValue)
    elif compAction == '==' and registers[compRegisterName] == compValue:
      registers,maxim = modifyRegister(maxim,incOrDec,registers,destRegisterName,destValue)
    elif compAction == '!=' and registers[compRegisterName] != compValue:
      registers,maxim = modifyRegister(maxim,incOrDec,registers,destRegisterName,destValue)
  return maxim

def modifyRegister(maxim,incOrDec,registers,registerName,registerValue):
  if incOrDec == 'inc':
    registers[registerName] += registerValue
  elif incOrDec == 'dec':
    registers[registerName] -= registerValue
  if registers[registerName] > maxim:
    maxim = registers[registerName]
  return registers,maxim

if __name__ == "__main__":
  inputs = readfileintowords("input.txt")
  print part1(inputs)
