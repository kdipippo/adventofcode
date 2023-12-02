def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def part1(inputstr):
  inputs = inputstr.split(",")
  inputs = [int(i) for i in inputs]
  inputs[1] = 12
  inputs[2] = 2
  i = 0
  while True:
    if inputs[i] == 1:
      inputs[inputs[i+3]] = inputs[inputs[i+1]] + inputs[inputs[i+2]]
    elif inputs[i] == 2:
      inputs[inputs[i+3]] = inputs[inputs[i+1]] * inputs[inputs[i+2]]
    elif inputs[i] == 99:
      return inputs
    i += 4


if __name__ == "__main__":
  # masses = [12, 14, 1969, 100756]
  strinputs = readfileintowords("input.txt")[0]
  example = "1,9,10,3,2,3,11,0,99,30,40,50"
  test1 = "1,0,0,0,99"
  test2 = "2,3,0,3,99"
  test3 = "1,1,1,4,99,5,6,0,99"
  # part1(example)
  # print part1(test3)
  result = part1(strinputs)
  print(result[0])