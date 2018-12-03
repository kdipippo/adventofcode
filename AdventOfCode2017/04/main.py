def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines

def part2(passphrases):
  count = 0
  for i in range(len(passphrases)):
    if not hasDuplicatesOrAnagrams(passphrases[i]):
      count += 1
  return count

def hasDuplicates(passphrase):
  passphrase.sort()
  for i in range(len(passphrase)-1):
    if passphrase[i] == passphrase[i+1]:
      return True
  return False

def hasDuplicatesOrAnagrams(passphrase):
  passphrase.sort()
  anagrams = []
  for i in range(len(passphrase)):
    if i < (len(passphrase)-1):
      if passphrase[i] == passphrase[i+1]:
        return True
    listphrase = list(passphrase[i])
    listphrase.sort()
    anagrams.append("".join(listphrase))
  anagrams.sort()
  print "$$ " + " ".join(passphrase) + " $$"
  print "## " + " ".join(anagrams) + " ##"
  for i in range(len(anagrams)-1):
    if anagrams[i] == anagrams[i+1]:
      print passphrase[i] + " == " + passphrase[i+1]
      return True
  return False

if __name__ == "__main__":
  passphrases = readfileintowords("input.txt")
  test = [['aa','bb','cc','dd','ee'],['aa','bb','cc','dd','aa'],['aa','bb','cc','dd','aaa']]
  #print part1(test)
  #print part1(passphrases)
  #print "-----"

  print hasDuplicatesOrAnagrams(['abcde','fghij'])
  print hasDuplicatesOrAnagrams(['abcde','xyz','ecdab'])
  print hasDuplicatesOrAnagrams(['a','ab','abc','abd','abf','abj'])
  print hasDuplicatesOrAnagrams(['iiii','oiii','ooii','oooi','oooo'])
  print hasDuplicatesOrAnagrams(['oiii','ioii','iioi','iiio'])
  print part2(passphrases)
