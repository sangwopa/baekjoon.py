def solution(s):
    answer = []
    tmp_lst = []
    tmp = ''
    for i in range(len(s[1:len(s)])):
        if s[i] == '{':
            continue
        elif s[i] == ',' and s[i-1] == '}':
            continue    
        elif s[i] == '}':
            tmp_lst.append(tmp.split(','))
            tmp = ''
        else:
            tmp += s[i]
    tmp_lst.sort(key=len)    
    for i in range(len(tmp_lst)):
        if i == 0:
            answer.append(int(tmp_lst[i][0]))
        else:
            for n in tmp_lst[i]:
                if not int(n) in answer:
                    answer.append(int(n))
                    break    
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))

s = "{{20,111},{111}}"
print(solution(s))

s = "{{123}}"
print(solution(s))

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
