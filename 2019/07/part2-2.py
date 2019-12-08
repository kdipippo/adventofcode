from itertools import permutations
import sys

# --------------------------------------------------
# Day 05 Work
# --------------------------------------------------

class Instruction:
  def __init__(self, inputs):
    self.optcode = inputs[0]
    self.param1mode = inputs[1]
    self.param2mode = inputs[2]
    self.param3mode = inputs[3]
  def getOptcode(self):
    return self.optcode
  def param1isImmediate(self):
    return self.param1mode == 1
  def param2isImmediate(self):
    return self.param2mode == 1
  def param3isImmediate(self):
    return self.param3mode == 1

class InputSignal:
  def __init__(self, firstSignal, secondSignal):
    self.firstSignal = firstSignal
    self.secondSignal = secondSignal
  def getSignal(self):
    if self.firstSignal is None:
      return self.secondSignal
    firstSig = self.firstSignal
    self.firstSignal = None
    return firstSig

class acsUnit():
  def __init__(self, inputs, phase, inputIndex):
    self.inputs = inputs
    self.phase = phase
    self.inputIndex = inputIndex
  def getInputs(self):
    return self.inputs
  def getPhase(self):
    return self.phase
  def getIndex(self):
    return self.inputIndex
  def update(self, newInputs, newIndex):
    self.inputs = newInputs
    self.inputIndex = newIndex

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def getOptcodesFromPrime(optcodePrime):
  optcodes = []
  optcodes.append(int(optcodePrime) % 100)
  optcodeStr = str(optcodePrime)[:-2]
  for optcode in reversed(optcodeStr):
    optcodes.append(int(optcode))
  while len(optcodes) < 4:
    optcodes.append(0)
  return optcodes

def getValueOfParams(instr, inputs, i):
  if instr.param1isImmediate():
    param1 = inputs[i+1]
    debug1 = str(param1)
  else:
    param1 = inputs[inputs[i+1]]
    debug1 = "inputs[" + str(inputs[i+1]) + "](which is " + str(param1) + ")"
  if instr.param2isImmediate():
    param2 = inputs[i+2]
    debug2 = str(param2)
  else:
    param2 = inputs[inputs[i+2]]
    debug2 = "inputs[" + str(inputs[i+2]) + "](which is " + str(param2) + ")"
  return param1, param2, debug1, debug2

def INTCODECOM(inputs, signal, index):
  i = index
  finalOutput = -1
  outputFlag = False
  debug = False
  while True:
    if debug:
      print(str(inputs[i]) + "(index " + str(i) + "), " + str(inputs[i+1]) + "(index " + str(i+1) + "), " + str(inputs[i+2]) + "(index " + str(i+2) + "), " + str(inputs[i+3]) + "(index " + str(i+3) + ")")
    instr = Instruction(getOptcodesFromPrime(inputs[i]))
    if outputFlag and instr.getOptcode() != 99:
      if debug:
        print("This code is still alive.")
      return finalOutput, inputs, i, False
    if instr.getOptcode() == 1:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      inputs[inputs[i+3]] = param1 + param2
      if debug:
        print("inputs[" + str(inputs[i+3]) + "] = " + debug1 + " + " + debug2)
      i += 4
    elif instr.getOptcode() == 2:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      inputs[inputs[i+3]] = param1 * param2
      if debug:
        print("inputs[" + str(inputs[i+3]) + "] = " + debug1 + " * " + debug2)
      i += 4
    elif instr.getOptcode() == 3:
      currSig = signal.getSignal()
      if debug:
        print("INPUT! - storing " + str(currSig) + " at index " + str(inputs[i+1]))
      inputs[inputs[i+1]] = currSig
      i += 2
    elif instr.getOptcode() == 4:
      if debug:
        print("OUTPUT! - returning " + str(inputs[inputs[i+1]]) + " at index " + str(inputs[i+1]))
      finalOutput = inputs[inputs[i+1]]
      outputFlag = True
      i += 2
    elif instr.getOptcode() == 5:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 != 0:
        if debug:
          print("jump-if-true: moving i from " + str(i) + " to " + debug2)
        i = param2
      else:
        if debug:
          print("jump-if-true failed because " + str(param1) + " == 0")
        i += 3
    elif instr.getOptcode() == 6:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 == 0:
        if debug:
          print("jump-if-false: moving i from " + str(i) + " to " + debug2)
        i = param2
      else:
        if debug:
          print("jump-if-false failed because " + str(param1) + " != 0")
        i += 3
    elif instr.getOptcode() == 7:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 < param2:
        if debug:
          print("inputs[" + str(inputs[i+3]) + "] = 1 because " + debug1 + " < " + debug2)
        inputs[inputs[i+3]] = 1
      else:
        if debug:
          print("inputs[" + str(inputs[i+3]) + "] = 0 because " + debug1 + " >= " + debug2)
        inputs[inputs[i+3]] = 0
      i += 4
    elif instr.getOptcode() == 8:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 == param2:
        if debug:
          print("inputs[" + str(inputs[i+3]) + "] = 1 because " + debug1 + " == " + debug2)
        inputs[inputs[i+3]] = 1
      else:
        if debug:
          print("inputs[" + str(inputs[i+3]) + "] = 0 because " + debug1 + " != " + debug2)
        inputs[inputs[i+3]] = 0
      i += 4
    elif instr.getOptcode() == 99:
      if debug:
        print("EXITING! - 99 found")
      return finalOutput, inputs, i, True
    else:
      if debug:
        print("UNKNOWN INSTRUCTION: " + str(inputs[i]))
      sys.exit(1)
    if debug:
      print("")
  return finalOutput, inputs, i

# --------------------------------------------------
# Day 07 Work
# --------------------------------------------------

def getPhasePermutations():
  return [list(p) for p in permutations(range(0, 5))]

def printAmpState(ampIsDead, ampName):
  if ampIsDead:
    print(ampName + " is dead")
  else:
    print(ampName + " is ALIVE")

def AMPLIFIERCONTROLSOFTWARE(inputs, sequence):
  # initialize acsUnits
  acsA = acsUnit(inputs, sequence[0], 0)
  acsB = acsUnit(inputs, sequence[1], 0)
  acsC = acsUnit(inputs, sequence[2], 0)
  acsD = acsUnit(inputs, sequence[3], 0)
  acsE = acsUnit(inputs, sequence[4], 0)
  ampE = 0
  AisDead = False
  BisDead = False
  CisDead = False
  DisDead = False
  EisDead = False

  # running each acsUnit intcode program
  for count in range(0,3):
    signalA = InputSignal(acsA.getPhase(), ampE)
    ampA, inputsA, indexA, AisDead = INTCODECOM(acsA.getInputs(), signalA, acsA.getIndex())
    acsA.update(inputsA, indexA)
    print("ampA --- " + str(ampA))
    signalB = InputSignal(acsB.getPhase(), ampA)
    ampB, inputsB, indexB, BisDead = INTCODECOM(acsB.getInputs(), signalB, acsB.getIndex())
    print("ampB --- " + str(ampB))
    signalC = InputSignal(acsC.getPhase(), ampB)
    ampC, inputsC, indexC, CisDead = INTCODECOM(acsC.getInputs(), signalC, acsC.getIndex())
    print("ampC --- " + str(ampC))
    signalD = InputSignal(acsD.getPhase(), ampC)
    ampD, inputsD, indexD, DisDead = INTCODECOM(acsD.getInputs(), signalD, acsD.getIndex())
    print("ampD --- " + str(ampD))
    signalE = InputSignal(acsE.getPhase(), ampD)
    ampE, inputsE, indexE, EisDead = INTCODECOM(acsE.getInputs(), signalE, acsE.getIndex())
    print("ampE --- " + str(ampE))
    print("----------")
    printAmpState(AisDead, "A")
    printAmpState(BisDead, "B")
    printAmpState(CisDead, "C")
    printAmpState(DisDead, "D")
    printAmpState(EisDead, "E")
  print("DONE!! -- " + str(ampE))
  return ampE

def testACS():
  inputstr = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
  inputs = inputstr.split(",")
  inputs = [int(i) for i in inputs]
  sequence = [9,8,7,6,5]
  AMPLIFIERCONTROLSOFTWARE(inputs, sequence)

def runAll(inputstr):
  inputs = inputstr.split(",")
  inputs = [int(i) for i in inputs]
  perms = getPhasePermutations()
  maxSignal = 0
  for sequence in perms:
    signal = AMPLIFIERCONTROLSOFTWARE(inputs, sequence)
    if signal > maxSignal:
      maxSignal = signal
  return maxSignal

if __name__ == "__main__":
  # inputstr = readfileintowords("input.txt")[0]
  # print(runAll(inputstr))
  testACS()