import math

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def fuelRequired(mass):
  return math.floor(mass / 3.0) - 2

if __name__ == "__main__":
  # masses = [12, 14, 1969, 100756]
  inputs = readfileintowords("input.txt")
  sum = 0
  for mass in inputs:
    fuel = fuelRequired(int(mass))
    while fuel > 0:
      sum += fuel
      fuel = fuelRequired(fuel)
  print sum