import glob
from node import Node
#import dijkstra as dj
import math
import itertools


def C(n,m):
  return (math.factorial(n))/(math.factorial(m)*math.factorial(n-m))



def cmpedgecost(e1,e2):
  if e1[2] > e2[2]:
    return 1
  elif e1[2] < e2[2]:
    return -1
  else:
    return 0

MAXNUM = 10**10

#last changes:
#tuple --> set2bits

def TSP(nodes,maxminedges):
  n = len(nodes)
  A = {}
  n0i = 0 
  n0 = nodes[n0i]
  t0 = tuple([n0i])
  for nd in nodes:
    ndi=nodes.index(nd)
    A[(set2bits([t0],n),ndi)] = MAXNUM
  A[(set2bits([t0],n),n0i)] = 0

  nodeindxs = range(0,n)

#  for m in range(2,n+1):
#    combs = itertools.combinations(nodeindxs[1:],m-1)
#    for c in combs:
#      S = [n0i]+list(c)
#      S.sort()
#      A[(tuple(S),n0i)] = MAXNUM

  An = {}

  for m in range(2,n+1):
    print "m=",m, "     n=",n
#    combs = itertools.combinations(nodes[1:],m-1)
    combs = itertools.combinations(nodeindxs[1:],m-1)
    for c in combs:
#      print "c from combs",c
      S = [n0i]+list(c)
      S.sort()
#      A[(set2bits(S),n0i)] = MAXNUM #initialization
      S1 = list(c)
      S1.sort()
      for nji in S1:
        nj = nodes[nji]
        mincost = MAXNUM
        for edge in nj.edges[0:maxminedges]:
          nki = edge[0]
          if nki == nji:
            nki = edge[1]

          if nki in S:
            ckj = edge[2]
            S2 = list(S)
            S2.remove(nji)
            if nki>0:
              Acst = A[(set2bits(S2,n),nki)]
            else: 
              if len(S2)==1:
                Acst = 0
              else:
                Acst = MAXNUM
            newcost = Acst + ckj
            if mincost > newcost:
              mincost = newcost
#              print "mincost:", mincost

        An[(set2bits(S,n),nji)] = mincost
    del A
    A = An
    An = {}
    
  Sf = set2bits(nodeindxs,n)
  mincost = MAXNUM
  for nx in nodes[1:]:
    nxi = nodes.index(nx)
    homeedge = None
    for edge in nx.edges:
      if edge[0] == n0i:
        homeedge = edge
      if edge[1] == n0i:
        homeedge = edge
    newcost = A[(Sf,nxi)] + homeedge[2]
    if mincost > newcost:
      mincost = newcost
  return mincost






def TSP2(nodes):
  import numpy as np
  import time
  n = len(nodes)
  A = np.zeros((2**n,n+1))
  n0i = 0 
  n0 = nodes[n0i]
  t0 = tuple([n0i])
  t0bits = set2bits([t0],n)
  for nd in nodes:
    ndi=nodes.index(nd)
    A[t0bits,ndi] = MAXNUM
  A[t0bits,n0i] = 0

  nodeindxs = range(0,n)


  for m in range(2,n+1):
    start_time = time.time()
    print "m=",m, "     n=",n
    fle = open("status.txt","w")
    fle.write("m= %s,     n= %s"%(str(m),str(n)))
    fle.close()
#    combs = itertools.combinations(nodes[1:],m-1)
    combs = itertools.combinations(nodeindxs[1:],m-1)
#    for c in combs:
#      S = [n0i]+list(c)
#      S.sort()
#      S1 = list(c)
#      S1.sort()
#      for nji in S1:
#        nj = nodes[nji]
#        mincost = MAXNUM
#        for edge in nj.edges[0:maxminedges]:
#          nki = edge[0]
#          if nki == nji:
#            nki = edge[1]
#          nk = nodes[nki]

#          if nki in S:
#            ckj = edge[2]
#            S2 = list(S)
#            S2.remove(nji)
#            if nki>0:
#              Acst = A[set2bits(S2,n),nki]
#            else: 
#              if len(S2)==1:
#                Acst = 0
#              else:
#                Acst = MAXNUM
#            newcost = Acst + ckj
#            if mincost > newcost:
#              mincost = newcost
#        A[set2bits(S,n),nji] = mincost
    for c in combs:
      S = set([n0i]+list(c))
      Sbits = set2bits(S,n)
      S1 = set(c)
      for nji in S1:
        nj = nodes[nji]
        mincost = MAXNUM
        Sj = set(S)
        Sj.remove(nji)
        Sjbits = set2bits(Sj,n)
        for nki in Sj:
#          nk = nodes[nki]
          ckj = nj.costs[nki]
          if nki>0:
            Acst = A[Sjbits,nki]
          else: 
            if len(Sj)==1:
              Acst = 0
            else:
              Acst = MAXNUM
          newcost = Acst + ckj
          if mincost > newcost:
            mincost = newcost
        A[Sbits,nji] = mincost
    print("    m=%i   --- %s seconds ---" % (m,time.time() - start_time))
   

  Sf = set2bits(nodeindxs,n)
  mincost = MAXNUM
  for nx in nodes[1:]:
    nxi = nodes.index(nx)
    homeedge = None
    for edge in nx.edges:
      if edge[0] == n0i:
        homeedge = edge
      if edge[1] == n0i:
        homeedge = edge
    newcost = A[Sf,nxi] + homeedge[2]
    if mincost > newcost:
      mincost = newcost
  return mincost






def TSP3(nodes):
  import time
  n = len(nodes)
  A = {}
  n0i = 0 
  n0 = nodes[n0i]
  t0 = tuple([n0i])
  t0bits = set2bits([t0],n)
  for nd in nodes:
    ndi=nodes.index(nd)
    A[(t0bits,ndi)] = MAXNUM
  A[(t0bits,n0i)] = 0

  nodeindxs = range(0,n)

#  for m in range(2,n+1):
#    combs = itertools.combinations(nodeindxs[1:],m-1)
#    for c in combs:
#      S = [n0i]+list(c)
#      S.sort()
#      A[(tuple(S),n0i)] = MAXNUM

  An = {}

  for m in range(2,n+1):
    start_time = time.time()
    print "m=",m, "     n=",n
    fle = open("status.txt","w")
    fle.write("m= %s,     n= %s \n"%(str(m),str(n)))
    fle.close()
   
    combs = itertools.combinations(nodeindxs[1:],m-1)
    numcombs = C(n-1,m-1)
    numcombsDiv100 = numcombs/100
    ci = 0
    for c in combs:
      ci+=1
      if numcombsDiv100>0 and ci%numcombsDiv100==0:
        ostri = "comb   %i   out of  %i"%((ci/numcombsDiv100)*numcombsDiv100,numcombs)
        print ostri
        
      S = set([n0i]+list(c))
      Sbits = set2bits(S,n)
      S1 = set(c)
      for nji in S1:
        nj = nodes[nji]
        mincost = MAXNUM
        Sj = set(S)
        Sj.remove(nji)
        Sjbits = set2bits(Sj,n)
        for nki in Sj:
#          nk = nodes[nki]
          ckj = nj.costs[nki]
          if nki>0:
            Acst = A[(Sjbits,nki)]
          else: 
            if len(Sj)==1:
              Acst = 0
            else:
              Acst = MAXNUM
          newcost = Acst + ckj
          if mincost > newcost:
            mincost = newcost
        An[(Sbits,nji)] = mincost
    del A
    A = An
    An = {}
    print("    m=%i   --- %s seconds ---" % (m,time.time() - start_time))
    
  Sf = set2bits(nodeindxs,n)
  mincost = MAXNUM
  for nx in nodes[1:]:
    nxi = nodes.index(nx)
    homeedgecost = nx.costs[0]
    newcost = A[(Sf,nxi)] + homeedgecost
    if mincost > newcost:
      mincost = newcost
  return mincost












def plot_nodes(nodes,filename):
    import matplotlib.pyplot as plt
    xsize = 5
    fig = plt.figure(1,(xsize, xsize*0.7/0.9))
    plt.subplots_adjust(bottom=0.15,left=0.175,right=0.95,top=0.95, hspace=0.001)
    for node in nodes:
      plt.plot(node.x, node.y, '.') 
      plt.text(node.x, node.y,str(node.num),fontsize=6,color='red')
    plt.savefig(filename)


def set2bits(st,n):
  res = 0
  for i in range(1,n+1):
    if i in st:
      res = res*2+1
    else:
      res = res*2
  return res

def bits2set(bits,n):
  st = set([0])
  l = range(1,n+1)
  l.reverse()
  for i in l:
    if bits%2 == 1:
      st.add(i)
    bits /= 2
  return st



#def merge_nodes(n1,n2,nodes,edges,edgesdct)

if(__name__=="__main__"):
  files = glob.glob("tsp.txt")
#  files = glob.glob("test.txt") 
#  files = glob.glob("test2.txt") 
#  files = glob.glob("test3.txt") 

  f = open(files[0])
  lines = f.readlines()
  f.close()

  l = lines[0]
  nums = l.strip().split(' ')
  numnodes = int(nums[0])
  print "numnodes: ", numnodes


  i = 0
  nodes = []
  for l in lines[1:]:
    nums = l.strip().split(' ')
    nums = [float(n) for n in nums]
    nodes.append(Node(i,nums[0],nums[1]))
    i += 1



  edgesdct = {}
  edges = []
  i=0
  while i < numnodes:
    ni = nodes[i]
    j=0
    while j < numnodes:
      nj = nodes[j]
      d = math.sqrt((ni.x-nj.x)**2+(ni.y-nj.y)**2)
      edge = [i,j,d]
      ni.costs.append(d)
      if not i==j:
        edges.append(edge)
        ni.edges.append(edge)
      j+=1
    i+=1

  for node in nodes:
    node.edges.sort(cmp=cmpedgecost)
#    print "node: ", node.num, "  edges:",node.edges[0:4]


#  plot_nodes(nodes,"cities.eps")


  print "numedges: ", len(edges)

#  mincost = TSP(nodes,len(nodes))
#  mincost = TSP(nodes,10)
#  mincost = TSP2(nodes)
  mincost = TSP3(nodes)
  print mincost

  fle = open("res.txt","w")
  fle.write("mincost = %s"%str(mincost))
  fle.close()

 
#  st = set([0,1,2,4,5,10])
#  n = 20
#  print "st:",st
#  bts = set2bits(st,n)
#  print "bits:",bts
#  st2 = bits2set(bts,n)
#  print "st2:",st2


#  A,negcycle = BellmanFord(nodes[0],nodes)
#  print "A[numnodes,:]=",A[numnodes,:].astype(np.int)
#  print "negcycle=",negcycle

  
#  minlen,negcycle = Johnsons(nodes,edges)
#  print "negcycle=",negcycle
#  print "minlen=",minlen




#def C(n,m):
#  return math.factorial(n)/(math.factorial(m)*math.factorial(n-m))

#for m in range(2,n+1):
#  print m,  C(n-1,m-1)*(m-1)**2

