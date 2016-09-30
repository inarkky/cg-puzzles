n, l, e = [int(i) for i in input().split()]
lstCon = []
lstNod = []
lst = []
lnt = []
a = ""
v = 0
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    lstCon.append([n1, n2])

for i in range(e):
    ei = int(input())
    lstNod.append(ei)

for i in range(len(lstCon)):
    for j in range(e):
        if lstNod[j] in lstCon[i]:
            lst.append( lstCon[i] )
        else:
            lnt.append( lstCon[i] )


while True:
    si = int(input())

    for i in range(len(lst)):
        if si in lst[i]:
            a = "{} {}".format(lst[i][0], lst[i][1])
            lst.pop(i)
            v = 1
            break
    if v == 0:
        for j in range(len(lnt)):
            if si in lnt[j]:
                a = "{} {}".format(lnt[j][0], lnt[j][1])
                lnt.pop(j)
                break
    print(a)
