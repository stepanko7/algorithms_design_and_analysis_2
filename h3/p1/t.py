

def knapsack_recurs(maxW,items,dictA,selitems):
    i = len(items)

    if dictA.has_key((i,maxW)):
        return dictA[(i,maxW)]

    if maxW <= 0:
        return 0,0
    if i == 0:
        return 0,0

    
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
    v1,w1 = knapsack_recurs(maxW,items[0:-1],dictA,selitems)
#    print "case1: i,v1,w1,maxW =",i,v1,w1,maxW

    #case2
    lastitem = items[-1]
    v = lastitem[0]
    w = lastitem[1]
    v2,w2 = knapsack_recurs(maxW-w,items[0:-1],dictA,selitems)
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

    return vtot,wtot




#f = open("knapsack_test2.txt","r")
#f = open("knapsack_test.txt","r")
f = open("knapsack1.txt","r")
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


selitems = []
dictA = {}
print knapsack_recurs(Wb,items,dictA,selitems)
