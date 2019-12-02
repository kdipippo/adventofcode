import itertools
import functools
import time

def readfileintowords(filename):
  with open(filename) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

def checkWord(word):
  worddict = {}
  for letter in word:
    if letter in worddict:
      worddict[letter] += 1
    else:
      worddict[letter] = 1
  return hasCount(2,worddict),hasCount(3,worddict)

def hasCount(count,worddict):
  for key in worddict:
    if worddict[key] == count:
      return True
  return False

def part1(wordlist):
  count2 = 0
  count3 = 0
  for word in wordlist:
    has2,has3 = checkWord(word)
    if has2:
      count2 += 1
    if has3:
      count3 += 1
  return count2*count3

def compareWord(word1,word2):
  if (word1 == word2):
    return 0
  count = 0
  for i in range(len(word1)):
    if word1[i] == word2[i]:
      count += 1
  return count

def compareWordComparator(pair1,pair2):
  compare1 = compareWord(pair1[0],pair1[1])
  compare2 = compareWord(pair2[0],pair2[1])
  if compare1 < compare2:
    return -1
  elif compare1 > compare2:
    return 1
  else:
    return 0

def part2(wordlist):
  pairlist = list(itertools.product(wordlist, wordlist))
  cmp = functools.cmp_to_key(compareWordComparator)
  pairlist.sort(key=cmp)
  finalword = ""
  for i in range(len(pairlist[-1][0])):
    if pairlist[-1][0][i] == pairlist[-1][1][i]:
      finalword += pairlist[-1][0][i]
  print(pairlist[-1][0])
  print(pairlist[-1][1])
  print(finalword)

if __name__ == "__main__":
  tests = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
  tests2 = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]
  inputs = readfileintowords("input.txt")
  start = time.time()
  part2(inputs)
  end = time.time()
  print(end - start)
