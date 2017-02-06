import sys
sys.setrecursionlimit(2500)
import numpy as np

def knapsack_recurs2(value,weight,maxW,items,dictA,maxVal):
    i = len(items)
#    print "i=",i

    if maxW < 0:
        return 0,0
    if i == 0:
        return 0,0

    if dictA.has_key((i,maxW)):
        return dictA[(i,maxW)]

#    lit = items[0]
#    valueratio = float(lit[0])/lit[1]
#    if maxW*valueratio + value < maxVal[0]:
#        return 0,0


#    if maxVal[0] < value:
#      maxVal[0] = value
#      print maxVal[0]

    
    if(i==1):
        item = items[i-1]
        v = item[0]
        w = item[1]
        valt = (0,0)
        if maxW >= w:
            valt = (v,w)

            if not dictA.has_key((i,w)):
                dictA[(1,w)] = valt

            if not dictA.has_key((i,maxW)):
                dictA[(1,maxW)] = valt
        else:
            valt = (0,0)
            if not dictA.has_key((i,maxW)):
                dictA[(1,maxW)] = valt
        return valt

    
    #case1
    v1,w1 = knapsack_recurs2(value,weight,maxW,items[0:-1],dictA,maxVal)
#    print "case1: i,v1,w1,maxW =",i,v1,w1,maxW

    #case2
    lastitem = items[-1]
    v = lastitem[0]
    w = lastitem[1]
    v2,w2 = knapsack_recurs2(value+v,weight+w,maxW-w,items[0:-1],dictA,maxVal)
    v2 += v 
    w2 += w
#    print "case1: i,v2,w2,maxW =",i,v2,w2,maxW

    vtot = 0
    wtot = 0
    if w2 > maxW:
        vtot = v1
        wtot = w1
    elif w1 > maxW:
        vtot = v2
        wtot = w2
    else:
        if v1 > v2:
            vtot = v1
            wtot = w1
        else:
            vtot = v2
            wtot = w2
        
    if not dictA.has_key((i,wtot)):
        dictA[(i,wtot)] = (vtot,wtot)
    if not dictA.has_key((i,maxW)):
        dictA[(i,maxW)] = (vtot,wtot)

    if maxVal[0] < vtot:
        maxVal[0] = vtot
        print maxVal[0]
    return vtot,wtot




#f = open("knapsack_test2.txt","r")
#f = open("knapsack_test.txt","r")
#f = open("knapsack1.txt","r")
f = open("knapsack_big.txt","r")
flines = f.readlines()

l1 = flines[0].split(" ")

Wb = int(l1[0])
N = int(l1[1])

print "Wb,N = ", Wb,N

items = []
for l in flines[1:]:
    tl = l.split(" ")
    v = int(tl[0])
    w = int(tl[1])
    items.append((v,w))

def itemcmp(x,y):
  if float(x[0])/x[1] > float(y[0])/y[1]:
    return -1
  else:
    return 1

items.sort(cmp=itemcmp)

maxW = Wb
maxVal = 0
maxWtmp = 0
for i in range(N):
  maxWtmp += items[i][1]
  if maxWtmp > maxW:
    break
  maxVal += items[i][0]


#print "items = ",items
print "maxVal:", maxVal


#cumsumval = {}
#cummaxval = {}
#cumsumval[0]=0
#cummaxval[0]=0
#sumv = 0
#for i in range(N):
#    sumv += items[i][0]
#    cumsumval[i] = sumv

dictA = {}
print knapsack_recurs2(0,0,Wb,items,dictA,[maxVal])

#Possible: (4243395, 1999783)

#BAD (4241988, 1997581) for problem2

#2493893  for problem1
