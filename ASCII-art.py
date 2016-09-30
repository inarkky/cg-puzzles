#init
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
l = int(input())
h = int(input())
t = input() #text source
o = ['']    #output
r = []

#fill
for d in range(h):
    inputed = input()
    r.append(inputed)
for i in range(h-1):
    o.append('')

#logic
for c in t:
    for idx, letter in enumerate(a):
        if c.upper() == letter:
            for i in range(h):
                o[i] += r[i][l * idx:l * (idx + 1)]
            break
    else:
        for i in range(h):
            o[i] += r[i][l * idx:l * (idx + 1)]

#print
for row in o:
    print (row)
