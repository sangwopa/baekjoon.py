maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

start = []
lever = []
exit = []

for i in range(len(maps)):
    for n in range(len(maps[i])):
        if maps[i][n] == 'X' or maps[i][n] == 'O':
            continue
        elif maps[i][n] == 'S':
            start = [i, n]
        elif maps[i][n] == 'L':
            lever = [i, n]
        elif maps[i][n] == 'E':
            exit = [i, n]
    
    if start != [] and lever != [] and exit != []:
        break
            


print("start: ", start)
print("lever: ", lever)
print("exit: ", exit)

