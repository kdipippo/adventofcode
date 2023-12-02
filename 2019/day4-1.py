def meetsCriteria(input):
  string = str(input)
  # It is a six-digit number.
  if len(string) != 6:
    return False
  # Going from left to right, the digits never decrease;
  #  they only ever increase or stay the same (like 111123 or 135679).
  prev = -1
  doubleFound = False
  for char in string:
    curr = int(char)
    if curr == prev:
      doubleFound = True
    if curr < prev:
      return False
    prev = curr
  # Two adjacent digits are the same (like 22 in 122345).
  return doubleFound

def part1(start, end):
  count = 0
  for i in range(start, end):
    if meetsCriteria(i):
      count += 1
  return count

if __name__ == "__main__":
  # print meetsCriteria(111111)
  # print meetsCriteria(223450)
  # print meetsCriteria(123789)
  print part1(367479, 893698)