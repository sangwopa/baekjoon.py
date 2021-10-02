N = int(input())

grp = []
for i in range(N):
    grp.append(str(input()))

def check_word(wrd):
    for i in range(len(wrd)-1):
        for n in range(i+1, len(wrd)):
            if wrd[i] == wrd[n]:
                flag = 0
            elif (flag == 1) and (wrd[i] == wrd[n]):
                flag = 2
            else:
                flag = 1
    if flag == 2:
        return False
    else:
        return True


