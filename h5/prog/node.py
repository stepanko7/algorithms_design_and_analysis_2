#class Node:
#  def __init__(self,n):
#    self.num = n
#    self.outedges = []
#    self.inedges = []
#    self.explored = False
#    self.f = -1


class Node:
  def __init__(self,n,x,y):
    self.num = n
    self.x = x
    self.y = y
#    self.outedges = []
#    self.inedges = []
    self.edges = []
    self.costs = []
#    self.explored = False
#    self.p = 0
#    self.f = -1

