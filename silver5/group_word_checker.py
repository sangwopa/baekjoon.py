N = int(input())

grp = []
for i in range(N):
    grp.append(str(input()))

def check_word(wrd):
    for i in range(len(wrd)-1):
        flag = 0
        for n in range(i+1, len(wrd)):
            if flag==1 and wrd[i]==wrd[n]:
                return False
            elif wrd[i] != wrd[n]:
                flag = 1
            else:
                flag = 0
    return True

cnt = 0
for i in range(N):
    if check_word(grp[i]) == True:
        cnt += 1

print(cnt)