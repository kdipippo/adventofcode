import time

def spinlock2(stepNum):
  #states = [0]
  zeroStates = [0, "-"]
  zeroPos = 0
  currentPos = 0
  stateNum = 1
  while stateNum <= 50000000:
    currentPos += stepNum
    currentPos %= stateNum #serves as size of states as well
    currentPos += 1
    #states.insert(currentPos,stateNum)
    if currentPos == zeroPos+1:
      zeroStates[1] = stateNum
    if currentPos < zeroPos:
      zeroPos += 1
    stateNum += 1
  print zeroStates


# MAIN ==============================
start_time = time.time()
spinlock2(314)
print("--- %s seconds ---" % (time.time() - start_time))
