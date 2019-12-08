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

def INTCODECOM(inputs, signal):
  i = 0
  finalOutput = -1
  while True:
    print(str(inputs[i]) + "(index " + str(i) + "), " + str(inputs[i+1]) + "(index " + str(i+1) + "), " + str(inputs[i+2]) + "(index " + str(i+2) + "), " + str(inputs[i+3]) + "(index " + str(i+3) + ")")
    instr = Instruction(getOptcodesFromPrime(inputs[i]))
    if instr.getOptcode() == 1:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      inputs[inputs[i+3]] = param1 + param2
      print("inputs[" + str(inputs[i+3]) + "] = " + debug1 + " + " + debug2)
      i += 4
    elif instr.getOptcode() == 2:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      inputs[inputs[i+3]] = param1 * param2
      print("inputs[" + str(inputs[i+3]) + "] = " + debug1 + " * " + debug2)
      i += 4
    elif instr.getOptcode() == 3:
      currSig = signal.getSignal()
      print("INPUT! - storing " + str(currSig) + " at index " + str(inputs[i+1]))
      inputs[inputs[i+1]] = currSig
      i += 2
    elif instr.getOptcode() == 4:
      print("OUTPUT! - returning " + str(inputs[inputs[i+1]]) + " at index " + str(inputs[i+1]))
      finalOutput = inputs[inputs[i+1]]
      i += 2
    elif instr.getOptcode() == 5:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 != 0:
        print("jump-if-true: moving i from " + str(i) + " to " + debug2)
        i = param2
      else:
        print("jump-if-true failed because " + str(param1) + " == 0")
        i += 3
    elif instr.getOptcode() == 6:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 == 0:
        print("jump-if-false: moving i from " + str(i) + " to " + debug2)
        i = param2
      else:
        print("jump-if-false failed because " + str(param1) + " != 0")
        i += 3
    elif instr.getOptcode() == 7:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 < param2:
        print("inputs[" + str(inputs[i+3]) + "] = 1 because " + debug1 + " < " + debug2)
        inputs[inputs[i+3]] = 1
      else:
        print("inputs[" + str(inputs[i+3]) + "] = 0 because " + debug1 + " >= " + debug2)
        inputs[inputs[i+3]] = 0
      i += 4
    elif instr.getOptcode() == 8:
      param1, param2, debug1, debug2 = getValueOfParams(instr, inputs, i)
      if param1 == param2:
        print("inputs[" + str(inputs[i+3]) + "] = 1 because " + debug1 + " == " + debug2)
        inputs[inputs[i+3]] = 1
      else:
        print("inputs[" + str(inputs[i+3]) + "] = 0 because " + debug1 + " != " + debug2)
        inputs[inputs[i+3]] = 0
      i += 4
    elif instr.getOptcode() == 99:
      print("EXITING! - 99 found")
      return finalOutput
    else:
      print("UNKNOWN INSTRUCTION: " + str(inputs[i]))
      sys.exit(1)
    print("")
  return finalOutput

# --------------------------------------------------
# Day 07 Work
# --------------------------------------------------

def getPhasePermutations():
  return [list(p) for p in permutations(range(0, 5))]

def AMPLIFIERCONTROLSOFTWARE(inputs, sequence):
  signalA = InputSignal(sequence[0], 0)
  ampA = INTCODECOM(inputs, signalA)
  signalB = InputSignal(sequence[1], ampA)
  ampB = INTCODECOM(inputs, signalB)
  signalC = InputSignal(sequence[2], ampB)
  ampC = INTCODECOM(inputs, signalC)
  signalD = InputSignal(sequence[3], ampC)
  ampD = INTCODECOM(inputs, signalD)
  signalE = InputSignal(sequence[4], ampD)
  ampE = INTCODECOM(inputs, signalE)
  return ampE

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
  inputstr = readfileintowords("input.txt")[0]
  print(runAll(inputstr))