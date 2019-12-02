class Tower:
  def __init__(self,name="",weight=0,children=[]):
    self.name = name
    self.weight = weight
    self.children = children

  def getName(self):
    return self.name

  def getWeight(self):
    return self.weight

  def getChildren(self):
    return self.children

  def addChild(self, newChild):
    self.children.append(newChild)

  def __str__(self):
    returnStr = self.name + " (" + str(self.weight) + ")"
    if len(self.children) > 0:
      returnStr += " -> "
      for i in range(len(self.children)-1):
        returnStr += self.children[i] + ", "
      returnStr += self.children[len(self.children)-1]
    return returnStr
