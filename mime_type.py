#deleting leading dot
def fix(line):
    return line[1:]
#using dict.get() to compare extensions
def output(d, e, i):
    el = ""
    el = d.get(fix(e[i]), "UNKNOWN")
    return el

d = {}
e = []
elem = ""
dotIdx = 0
n = int(input())
q = int(input())

#creating dict ["extension": "mime"]
for i in range(n):
    ext, mt = input().split()
    d[ext.lower()] = mt

#geting extension from filename
#storing into a variable (space - separated)
for i in range(q):
    fname = input()
    dotIdx = fname.rfind('.')
    elem += fname[dotIdx::1].lower()
    elem += " "

#making a list from string
e = elem.split(" ")
for i in range(q):
    print(output(d, e, i))
