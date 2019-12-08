import sys

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def chunkstring(string, length):
  return (string[0+i:length+i] for i in range(0, len(string), length))

def getCellResult(col):
  for i in range(len(col)):
    if col[i] == "0":
      return "."
    elif col[i] == "1":
      return "#"
  return ""

def run(inputStr, wide, tall):
  photoLayers = list(chunkstring(inputStr, (wide * tall)))
  flatPhoto = ""
  for i in range(len(photoLayers[0])):
    col = "".join([x[i] for x in photoLayers])
    flatPhoto += getCellResult(col)
  photoRows = list(chunkstring(flatPhoto, (wide)))
  for row in photoRows:
    print(row)

if __name__ == "__main__":
  inputStr = readfileintowords("input.txt")[0]
  run(inputStr, 25, 6)
  # run("0222112222120000", 2, 2)