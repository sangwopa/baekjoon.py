def check_word(wrd):
    flag = 0
    for i in range(len(wrd)-1):
        for n in range(i+1, len(wrd)):
            if wrd[i] == wrd[n]:
                flag = 0
            elif flag == 1 or wrd[i] == wrd[n]:
                flag = 2
                return False
            elif wrd[i] != wrd[n]:
                flag = 1
            else:
                flag = 0
    print(flag)
    if flag == 2:
        return False
    else:
        return True

print(check_word('aba'))