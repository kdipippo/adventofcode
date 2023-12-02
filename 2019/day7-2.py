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
  def __init__(self, sequenceSignal, ampSignal):
    self.signals = []
    self.signals.append(sequenceSignal)
    self.signals.append(ampSignal)
  def getSignal(self):
    firstSig = self.signals[0]
    self.signals.pop(0)
    return firstSig
  def appendSignal(self, newSignal):
    self.signals.append(newSignal)

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

def INTCODECOM(inputs, signal, printMessages):
  i = 0
  finalOutput = -1
  while True:
    # if printMessages:
    #   print(str(inputs[i]) + "(index " + str(i) + "), " + str(inputs[i+1]) + "(index " + str(i+1) + "), " + str(inputs[i+2]) + "(index " + str(i+2) + "), " + str(inputs[i+3]) + "(index " + str(i+3) + ")")
    instr = Instruction(getOptcodesFromPrime(inputs[i]))
    if instr.getOptcode() == 1:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      inputs[inputs[i+3]] = param1 + param2
      if printMessages:
        print("inputs[" + str(inputs[i+3]) + "] = " + debug1 + " + " + debug2)
      i += 4
    elif instr.getOptcode() == 2:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      inputs[inputs[i+3]] = param1 * param2
      if printMessages:
        print("inputs[" + str(inputs[i+3]) + "] = " + debug1 + " * " + debug2)
      i += 4
    elif instr.getOptcode() == 3:
      currSig = signal.getSignal()
      if printMessages:
        print("INPUT! - storing " + str(currSig) + " at index " + str(inputs[i+1]))
      inputs[inputs[i+1]] = currSig
      i += 2
    elif instr.getOptcode() == 4:
      if printMessages:
        print("OUTPUT! - returning " + str(inputs[inputs[i+1]]) + " at index " + str(inputs[i+1]))
      finalOutput = inputs[inputs[i+1]]
      signal.appendSignal(inputs[inputs[i+1]])
      i += 2
    elif instr.getOptcode() == 5:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 != 0:
        if printMessages:
          print("jump-if-true: moving i from " + str(i) + " to " + debug2)
        i = param2
      else:
        if printMessages:
          print("jump-if-true failed because " + str(param1) + " == 0")
        i += 3
    elif instr.getOptcode() == 6:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 == 0:
        if printMessages:
          print("jump-if-false: moving i from " + str(i) + " to " + debug2)
        i = param2
      else:
        if printMessages:
          print("jump-if-false failed because " + str(param1) + " != 0")
        i += 3
    elif instr.getOptcode() == 7:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 < param2:
        if printMessages:
          print("inputs[" + str(inputs[i+3]) + "] = 1 because " + debug1 + " < " + debug2)
        inputs[inputs[i+3]] = 1
      else:
        if printMessages:
          print("inputs[" + str(inputs[i+3]) + "] = 0 because " + debug1 + " >= " + debug2)
        inputs[inputs[i+3]] = 0
      i += 4
    elif instr.getOptcode() == 8:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 == param2:
        if printMessages:
          print("inputs[" + str(inputs[i+3]) + "] = 1 because " + debug1 + " == " + debug2)
        inputs[inputs[i+3]] = 1
      else:
        if printMessages:
          print("inputs[" + str(inputs[i+3]) + "] = 0 because " + debug1 + " != " + debug2)
        inputs[inputs[i+3]] = 0
      i += 4
    elif instr.getOptcode() == 99:
      if printMessages:
        print("EXITING! - 99 found")
      return finalOutput, inputs
    else:
      if printMessages:
        print("UNKNOWN INSTRUCTION: " + str(inputs[i]))
      sys.exit(1)
    # if printMessages:
    #   print("")
  return finalOutput, inputs

# --------------------------------------------------
# Day 07 Work
# --------------------------------------------------

def getPhasePermutations():
  return [list(p) for p in permutations(range(5, 10))]

def AMPLIFIERCONTROLSOFTWARE(inputs, sequence):
  amp = 0
  i = 0
  debug = True
  while True:
    i = i % len(sequence)
    signal = InputSignal(sequence[i], amp)
    amp = INTCODECOM(inputs, signal, debug)
    i += 1

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

def testACS(inputstr, sequence):
  inputs = inputstr.split(",")
  inputs = [int(i) for i in inputs]
  amp = 0
  i = 0
  signal = InputSignal(9, 0)
  amp, inputs = INTCODECOM(inputs, signal, True)
  print("~~~~~~~~" + str(amp) + "~~~~~~~~~")
  print(inputs)

if __name__ == "__main__":
  # inputstr = readfileintowords("input.txt")[0]
  # print(runAll(inputstr))
  program = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
  sequence = [9,8,7,6,5]
  testACS(program, sequence)