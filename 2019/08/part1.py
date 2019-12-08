import sys

'''
This is actually the second iteration of this puzzle that I attempted.
I first tried storing the layers and cells in a 3-dimensional array and
then creating a class to manage everything; but the actual ask for part 1
helped me figure out I can just split the string into evenly-sized chunks.
'''

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def chunkstring(string, length):
  return (string[0+i:length+i] for i in range(0, len(string), length))

def run(inputStr, wide, tall):
  photoLayers = list(chunkstring(inputStr, (wide * tall)))
  minZeroes = sys.maxint
  minZeroesLayer = ""
  for layer in photoLayers:
    zeroCount = layer.count("0")
    if zeroCount < minZeroes:
      minZeroes = zeroCount
      minZeroesLayer = layer
  print(minZeroesLayer.count("1") * minZeroesLayer.count("2"))

if __name__ == "__main__":
  inputStr = readfileintowords("input.txt")[0]
  # run("123456789012", 3, 2)
  run(inputStr, 25, 6)