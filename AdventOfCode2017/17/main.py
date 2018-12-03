from Node import *
from UnorderedList import *

# part 1's version thats inefficient
def spinlock(stepNum):
  states = [0]
  currentPos = 0
  stateNum = 1
  while stateNum < 50000001:
    if stateNum%10000 == 0:
      print stateNum
    currentPos += stepNum
    currentPos %= len(states)
    currentPos += 1
    states.insert(currentPos,stateNum)
    stateNum += 1
  yearIndex = states.index(0)
  print states[yearIndex-1]
  print states[yearIndex]
  print states[yearIndex+1]

# part 2, using linked lists
def spinlockLinkedList(stepNum):
  states = UnorderedList()
  states.append(0)
  statesSize = 1
  currentPos = 0
  stateNum = 1
  while stateNum < 10:
    currentPos += stepNum
    currentPos %= statesSize
    currentPos += 1
    print "Inserting into " + str(currentPos)
    if statesSize == 1:
      states.append(stateNum)
    else:
      states.insert(currentPos,stateNum)
    statesSize += 1
    stateNum += 1
    print states

if __name__ == "__main__":
  spinlockLinkedList(3)
