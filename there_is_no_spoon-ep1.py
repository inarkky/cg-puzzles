width = int(input())
height = int(input())
col = []
for i in range(height):
    line = input()
    col.append(list(line))

for i in range(height):
    for j in range(width):
        if col[i][j] == "0":
            tmpEx, tmpEy = -1, -1
            tmpSx, tmpSy = -1, -1
            for z in range(j+1, width):
                if (col[i][z] == "0"):
                    tmpEx, tmpEy = z, i
                    break
            for z in range(i+1, height):
                if (col[z][j] == "0"):
                    tmpSx, tmpSy = j, z
                    break
            print( "{} {} {} {} {} {}".format(j, i, tmpEx, tmpEy, tmpSx, tmpSy) )
