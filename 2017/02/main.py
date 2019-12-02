def part1(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  sum = 0
  for i in range(0, len(content)):
    row = content[i].split("\t")
    min = 99999999999999999999999999
    max = -1
    for j in range(0, len(row)):
      if int(row[j]) < min:
        min = int(row[j])
      if int(row[j]) > max:
        max = int(row[j])
    sum += abs(max-min)
    print sum
  return sum

def part2(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  sum = 0
  for i in range(0, len(content)):
    row = content[i].split("\t")
    for j in range(0, len(row)):
      row[j] = int(row[j])
    sum += findEven(row)
    print sum
  return sum

def findEven(row):
  for i in range(0,len(row)):
    for j in range(0,len(row)):
      if ((i != j) and (row[i]%row[j]==0 or row[j]%row[i]==0)):
        if row[i]%row[j]==0:
          return row[i]/row[j]
        else:
          return row[j]/row[i]


if __name__ == "__main__":
  #print part2("test.txt")
  print part2("input.txt")
