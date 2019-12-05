def meetsCriteria(input):
  string = str(input)
  # It is a six-digit number.
  if len(string) != 6:
    return False
  numCounts = dict()
  # only check for escalating numbers and track number frequencies
  prev = -1
  for char in string:
    curr = int(char)
    if curr not in numCounts:
      numCounts[curr] = 0
    numCounts[curr] += 1
    if curr < prev:
      return False
    prev = curr
  if 2 in numCounts.values():
    return True
  return False

def part2(start, end):
  count = 0
  for i in range(start, end):
    if meetsCriteria(i):
      count += 1
  return count

if __name__ == "__main__":
  # print meetsCriteria(112233)
  # print meetsCriteria(123444)
  # print meetsCriteria(111122)
  print part2(367479, 893698)