import sys
sys.setrecursionlimit(2500)
import numpy as np

def knapsack_recurs2(value,weight,maxW,items,dictV,dictW,maxVal):
    i = len(items)
#    print "i=",i

    lit = items[0]
    valueratio = float(lit[0])/lit[1]
    if maxW*valueratio + value < maxVal[0]:
#        print "maxW,valueratio,value,maxVal[0]",maxW,valueratio,value,maxVal[0]
        return 0,0

    if dictV[i,maxW]>0:
        return dictV[i,maxW], dictW[i,maxW]

    if maxW < 0:
        return 0,0
    if i == 0:
        return 0,0

    if maxVal[0] < value:
      maxVal[0] = value

    
    if(i==1):
        item = items[i-1]
        v = item[0]
        w = item[1]
        valt = (0,0)
        if maxW >= w:
            valt = (v,w)

            if dictV[i,w]==-1:
                dictV[(1,w)] = valt[0]
                dictW[(1,w)] = valt[1]

            if dictV[i,maxW]==-1:
                dictV[1,maxW] = valt[0]
                dictW[(1,maxW)] = valt[1]
        else:
            valt = (0,0)
            if dictV[i,maxW]==-1:
                dictV[1,maxW] = valt[0]
                dictW[(1,maxW)] = valt[1]
        return valt

    
    #case1
    v1,w1 = knapsack_recurs2(value,weight,maxW,items[0:-1],dictV,dictW,maxVal)
#    print "case1: i,v1,w1,maxW =",i,v1,w1,maxW

    #case2
    lastitem = items[-1]
    v = lastitem[0]
    w = lastitem[1]
    v2,w2 = knapsack_recurs2(value+v,weight+w,maxW-w,items[0:-1],dictV,dictW,maxVal)
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
        
    if dictV[i,wtot]==-1:
        dictV[(i,wtot)] = vtot
        dictW[(i,wtot)] = wtot
    if dictV[i,maxW]==-1:
        dictV[(i,maxW)] = vtot
        dictW[(i,maxW)] = wtot

#    if maxval[0] < vtot:
#        maxval[0] = vtot
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

dictV = np.ones((N+1,Wb+1))
dictW = np.ones((N+1,Wb+1))
dictV = -dictV
dictW = dictW*0
print knapsack_recurs2(0,0,Wb,items,dictV,dictW,[maxVal])



#2493893  for problem1
