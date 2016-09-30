n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

temps_list = temps.split()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
if not temps_list:
    rez = 0
else:
    tmp = [int(i) for i in temps_list]
    rez = min(tmp, key=lambda x:abs(x-0))
    if abs(rez) in tmp:
        rez = abs(rez)


print(rez)
