from Node import *

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self,item):
      newNode = Node(item)
      if self.head == None:
        self.head = newNode
      else:
        current = self.head
        while current.getNext() != None:
          current = current.getNext()
        current.setNext(newNode)

    def size(self):
        return self.size

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def __str__(self):
      listStr = "LIST: "
      current = self.head
      listStr += str(current.getData()) + " "
      while current.getNext() != None:
        current = current.getNext()
        listStr += str(current.getData()) + " "
      return listStr

    def insert(self,finalPos,stateNum):
      newNode = Node(stateNum)
      current = self.head
      currentIndex = 0
      while current.getNext() != None and currentIndex <= finalPos:
        current = current.getNext()
      # BEFORE current.next -> nextNode
      # AFTER  current.next -> newNode.next -> nextNode
      nextNode = current.getNext()
      current.setNext(newNode)
      newNode.setNext(nextNode)
