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

def processOpcodes(inputs, id):
  i = 0
  while True:
    instr = Instruction(getOptcodesFromPrime(inputs[i]))
    if instr.getOptcode() == 1:
      # print("1 [" + str(inputs[i]) + "] --------")
      # print(str([inputs[i]]) + "," + str([inputs[i+1]]) + "," + str([inputs[i+2]]) + "," + str([inputs[i+3]]))
      if instr.param1isImmediate():
        param1 = inputs[i+1]
        debugstr = " = " + str(param1)
      else:
        param1 = inputs[inputs[i+1]]
        debugstr = " = inputs[" + str(inputs[i+1]) + "](which is " + str(param1) + ")"
      if instr.param2isImmediate():
        param2 = inputs[i+2]
        debugstr2 = " = " + str(param2)
      else:
        param2 = inputs[inputs[i+2]]
        debugstr2 = " + inputs[" + str(inputs[i+2]) + "](which is " + str(param2) + ")"
      inputs[inputs[i+3]] = param1 + param2
      print("inputs[" + str(inputs[i+3]) + "]" + debugstr + debugstr2)
      i += 4
    elif instr.getOptcode() == 2:
      # print("2 [" + str(inputs[i]) + "] --------")
      # print(str([inputs[i]]) + "," + str([inputs[i+1]]) + "," + str([inputs[i+2]]) + "," + str([inputs[i+3]]))
      if instr.param1isImmediate():
        param1 = inputs[i+1]
        debugstr = " = " + str(param1)
      else:
        param1 = inputs[inputs[i+1]]
        debugstr = " = inputs[" + str(inputs[i+1]) + "](which is " + str(param1) + ")"
      if instr.param2isImmediate():
        param2 = inputs[i+2]
        debugstr2 = " = " + str(param2)
      else:
        param2 = inputs[inputs[i+2]]
        debugstr2 = " * inputs[" + str(inputs[i+2]) + "](which is " + str(param2) + ")"
      inputs[inputs[i+3]] = param1 * param2
      print("inputs[" + str(i+3) + "]" + debugstr + debugstr2)
      i += 4
    elif instr.getOptcode() == 3:
      # print("3 [" + str(inputs[i]) + "] --------")
      print ("INPUT! - storing " + str(id) + " at index " + str(inputs[i+1]))
      inputs[inputs[i+1]] = id
      i += 2
    elif instr.getOptcode() == 4:
      # print("4 [" + str(inputs[i]) + "] --------")
      print ("OUTPUT! - returning " + str(inputs[inputs[i+1]]) + " at index " + str(inputs[i+1]))
      i += 2
    elif instr.getOptcode() == 99:
      # print("99 [" + str(inputs[i]) + "] --------")
      print ("EXITING! - 99 found")
      return inputs

def TEST(inputstr, id):
  inputs = inputstr.split(",")
  inputs = [int(i) for i in inputs]
  return processOpcodes(inputs, id)

if __name__ == "__main__":
  inputstr = readfileintowords("input.txt")[0]
  id = 1
  result = TEST(inputstr, id)
  # print(result)