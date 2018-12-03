def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines

def isInt(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def soundDuet(instructions):
  registers = {}
  i = 0 # instruction index
  recoveredFrequency = 0
  jumpFlag = False
  totalCount = 1

  while True:
    print i,
    print "\t",
    print instructions[i],
    print "\t",
    jumpFlag = False
    if instructions[i][1] not in registers:
      registers[instructions[i][1]] = 0
    if instructions[i][0] == "snd":
      recoveredFrequency = registers[instructions[i][1]]
    elif instructions[i][0] == "set":
      if isInt(instructions[i][2]):
        registers[instructions[i][1]] = int(instructions[i][2])
      else:
        registers[instructions[i][1]] = registers[instructions[i][2]]
    elif instructions[i][0] == "add":
      if isInt(instructions[i][2]):
        registers[instructions[i][1]] += int(instructions[i][2])
      else:
        registers[instructions[i][1]] += registers[instructions[i][2]]
    elif instructions[i][0] == "mul":
      if isInt(instructions[i][2]):
        registers[instructions[i][1]] *= int(instructions[i][2])
      else:
        registers[instructions[i][1]] *= registers[instructions[i][2]]
    elif instructions[i][0] == "mod":
      if isInt(instructions[i][2]):
        registers[instructions[i][1]] = registers[instructions[i][1]] % int(instructions[i][2])
      else:
        registers[instructions[i][1]] = registers[instructions[i][1]] % registers[instructions[i][2]]
    elif instructions[i][0] == "rcv":
      if registers[instructions[i][1]] != 0:
        print
        print "TOTAL COUNT = " + str(totalCount)
        return recoveredFrequency
    elif instructions[i][0] == "jgz":
      if registers[instructions[i][1]] > 0:
        i += int(instructions[i][2])
        jumpFlag = True
    if not jumpFlag:
      i += 1
    print registers
    totalCount += 1

def thisIsDeadlock(instructions,reg1Index,reg2Index,reg1sendQueue,reg2sendQueue):
  if len(reg1sendQueue) == 0 and len(reg2sendQueue) == 0:
    if instructions[reg1Index][0] == "rcv" and instructions[reg2Index][0] == "rcv":
      return True
  return False

def twoDuet(instructions):
  registers1 = {}
  registers1["p"] = 0
  registers2 = {}
  registers2["p"] = 1
  reg1sendQueue = []
  reg2sendQueue = []
  reg1Index = 0
  reg2Index = 0

  reg1SendCounter = 0

  while True:
    if reg1Index < 10:
      print " #" + str(reg1Index),
    else:
      print "#" + str(reg1Index),
    print " queue1=" + str(len(reg1sendQueue))
    if reg2Index < 10:
      print " #" + str(reg2Index),
    else:
      print "#" + str(reg2Index),
    print " queue2=" + str(len(reg2sendQueue))
    print

    if thisIsDeadlock(instructions,reg1Index,reg2Index,reg1sendQueue,reg2sendQueue):
      print
      print "registers1 sent " + str(reg1SendCounter) + "!!!!!"
      return "DEADLOCK"

    if not isInt(instructions[reg1Index][1]):
      if instructions[reg1Index][1] not in registers1:
        registers1[instructions[reg1Index][1]] = 0
    if not isInt(instructions[reg2Index][1]):
      if instructions[reg2Index][1] not in registers2:
        registers2[instructions[reg2Index][1]] = 0

    # REGISTER 1
    if instructions[reg1Index][0] == "snd":
      if isInt(instructions[reg1Index][1]):
        reg1sendQueue.append(int(instructions[reg1Index][1]))
      else:
        reg1sendQueue.append(int(registers1[instructions[reg1Index][1]]))
      reg1Index += 1
    elif instructions[reg1Index][0] == "rcv":
      if len(reg2sendQueue)>0:
        registers1[instructions[reg1Index][1]] = reg2sendQueue[0]
        reg2sendQueue.pop(0)
        reg1Index += 1
    else:
      registers1, reg1Index = miscRegisterActions(registers1,instructions[reg1Index],reg1Index)

    # REGISTER 2
    if instructions[reg2Index][0] == "snd":
      if isInt(instructions[reg2Index][1]):
        reg2sendQueue.append(int(instructions[reg2Index][1]))
      else:
        reg2sendQueue.append(registers2[instructions[reg2Index][1]])
      reg2Index += 1
    elif instructions[reg2Index][0] == "rcv":
      if len(reg1sendQueue)>0:
        registers2[instructions[reg2Index][1]] = reg1sendQueue[0]
        reg1sendQueue.pop(0)
        reg1SendCounter += 1
        reg2Index += 1
    else:
      registers2, reg2Index = miscRegisterActions(registers2,instructions[reg2Index],reg2Index)
  if reg1Index < 10:
    print " #" + str(reg1Index),
  else:
    print "#" + str(reg1Index),
  print " queue1=" + str(len(reg1sendQueue)),
  print "\t",
  if reg2Index < 10:
    print " #" + str(reg2Index),
  else:
    print "#" + str(reg2Index),
  print " queue2=" + str(len(reg1sendQueue))
  print "==1: ",
  print instructions[reg1Index],
  print "  ",
  print registers1
  print reg1sendQueue
  print "==2: ",
  print instructions[reg2Index],
  print "  ",
  print registers2
  print reg2sendQueue

def miscRegisterActions(registers,instrRow,regIndex):
  jumpFlag = False
  if instrRow[0] == "set":
    if isInt(instrRow[2]):
      registers[instrRow[1]] = int(instrRow[2])
    else:
      registers[instrRow[1]] = registers[instrRow[2]]
  elif instrRow[0] == "add":
    if isInt(instrRow[2]):
      registers[instrRow[1]] += int(instrRow[2])
    else:
      registers[instrRow[1]] += registers[instrRow[2]]
  elif instrRow[0] == "mul":
    if isInt(instrRow[2]):
      registers[instrRow[1]] *= int(instrRow[2])
    else:
      registers[instrRow[1]] *= registers[instrRow[2]]
  elif instrRow[0] == "mod":
    if isInt(instrRow[2]):
      registers[instrRow[1]] = registers[instrRow[1]] % int(instrRow[2])
    else:
      registers[instrRow[1]] = registers[instrRow[1]] % registers[instrRow[2]]
  elif instrRow[0] == "jgz":
    if ((isInt(instrRow[1]) and int(instrRow[1])>0) or ((not isInt(instrRow[1])) and (registers[instrRow[1]] > 0))):
      if isInt(instrRow[2]):
        regIndex += int(instrRow[2])
      else:
        regIndex += int(registers[instrRow[2]])
      jumpFlag = True
  if not jumpFlag:
    regIndex += 1
  return registers,regIndex

instr = readfileintowords("input.txt")
print twoDuet(instr)
