def part1(generatorA, generatorB):
  judge = 0
  for i in range(100):
    print "Finished " + str(i) + "%"
    for j in range(50000):
      generatorA = (generatorA*16807)%2147483647
      while (generatorA%4 != 0):
        generatorA = (generatorA*16807)%2147483647

      generatorB = (generatorB*48271)%2147483647
      while (generatorB%8 != 0):
        generatorB = (generatorB*48271)%2147483647
      '[
        }'
      binA = bin(generatorA)[-16:]
      while len(binA) < 16:
        binA = "0" + binA
      binB = bin(generatorB)[-16:]
      while len(binB) < 16:
        binB = "0" + binB

      if binA == binB:
        #print getBinStr(generatorA),getBinStr(generatorB)
        judge += 1
  print "Judgement: " + str(judge)

if __name__ == "__main__":
  #part1(65,8921) #test
  part1(873,583) #puzz
