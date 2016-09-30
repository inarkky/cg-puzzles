def findIdxs(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def fixer(x):
    fix = ""
    for item in x:
        if len(item) < 7:
            item = "0" + item
        fix += item
    return fix
    

def composeList(a, x):
    scratch = ""
    z = 0
    for i, letter in enumerate(x):
        if letter == "1":
            if letter == x[i-1] and i > 0:
                scratch += "0"
            else:
                scratch += " 0 0"
        elif letter == "0":
            if letter == x[i-1] and i > 0:
                scratch += "0"
            else:
                scratch += " 00 0"
        fixed = scratch[1:len(scratch)]
    return "{}".format(fixed)


message = input()
string = (' '.join(format(ord(x), 'b') for x in message)).split()
fixed = fixer(string)
output = ""

ones = findIdxs(fixed, "1")
output += composeList(ones, fixed)

output += "\n"

print(output)

