def solution(s):
    tmp = s.split(' ')
    lst = []
    for i in tmp:
        if i == '':
            lst.append(' ')
        else:
            lst.append(i[0].upper() + i[1:].lower())
    con = ''
    print(lst)
    for i, n in enumerate(lst):
        if i == (len(lst)-1):
            con += n
            break
        if (lst[i] != ' ') and (lst[i+1] != ' '):
            con += n + ' '
        else:
            con += n
    return con

print(solution("3people  unFollowed me"))
print(solution("for the last week"))
print(solution(" "))
print(solution(" "))