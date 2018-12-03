def readfileintosentences(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  for i in range(0,len(content)):
    content[i] = content[i].split(" ")
  return content

def getDay1(numbers):
  numberslist = []
  for i in range(0, len(numbers)):
    numberslist.append(int(numbers[i]))

  sum = 0
  i = 0
  while i < (len(numberslist)-1):
    if numberslist[i] == numberslist[i+1]:
      sum += numberslist[i]
    i+=1
  if numberslist[-1] == numberslist[0]:
    sum += numberslist[-1]
  #return str(numbers) + " result is " + str(sum)
  return sum

def day1part2(numbers):
  numberslist = []
  for i in range(0, len(numbers)):
    numberslist.append(int(numbers[i]))

  numberlength = len(numberslist)
  halfnumberlength = numberlength/2
  sum = 0
  i = 0
  while i < (len(numberslist)):
    if numberslist[(i%numberlength)] == numberslist[((i+halfnumberlength)%numberlength)]:
      sum += numberslist[i]
    i+=1
  return sum


if __name__ == "__main__":
  numbers = readfileintosentences("input.txt")[0]
  print day1part2('1212') == 6
  print day1part2('1221') == 0
  print day1part2('123425') == 4
  print day1part2('123123') == 12
  print day1part2('12131415') == 4
  print day1part2(numbers)
