def solution(s):
    lst = []
    tmp = ''
    for i, n in enumerate(s):
        if n == ' ':
            lst.append(n)
            if len(tmp)>1:
                lst.append(tmp[0].upper() + tmp[1:].lower())
            elif len(tmp) == 1:
                lst.append(tmp[0].upper())    
            else:
                lst.append(tmp)    
            tmp = ''
        if n != ' ':
            tmp += n
        if i == (len(s) - 1):
            if len(tmp)>1:
                lst.append(' ')
                lst.append(tmp[0].upper() + tmp[1:].lower())
            elif len(tmp) == 1:
                lst.append(' ')
                lst.append(tmp[0].upper())    
            else:
                lst.append(' ')
                lst.append(tmp) 
                    
    return ''.join(lst)[1:]

print(solution(" 3people  unFollowed me"))
print(solution("for the last week"))
print(solution(" "))
print(solution(" "))
            