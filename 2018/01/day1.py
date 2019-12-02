import time

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def part2_lists(inputs):
  start = 0
  prevFreqs = []
  prevFreqs.append(start)
  i = 0
  while (True):
    start += int(inputs[i])
    if start in prevFreqs:
      return start
    else:
      prevFreqs.append(start)
    #print(start)
    #print(prevFreqs)
    i += 1
    if i == len(inputs)-1:
        print("new cycle - " + str(len(prevFreqs)))
    i = i % len(inputs)

def part2_sets(inputs):
  start = 0
  prevFreqs = set()
  prevFreqs.add(start)
  i = 0
  while (True):
    start += int(inputs[i])
    if start in prevFreqs:
      print("prevFreqs str = " + str(len(prevFreqs)))
      return start
    else:
      prevFreqs.add(start)
    #print(start)
    #print(prevFreqs)
    i += 1
    if i == len(inputs)-1:
        print("new cycle - " + str(len(prevFreqs)))
    i = i % len(inputs)

if __name__ == "__main__":
  inputs = readfileintowords("input.txt")
  start = time.time()
  print(part2_sets(inputs))
  end = time.time()
  print(end - start)
