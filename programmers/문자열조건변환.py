def solution(s):
    answer = ''
    lst = s.split(' ')
    new_lst = []

    for i in lst:
        tmp = ''
        for n in range(len(i)):
            if (n % 2) == 0:
                tmp += i[n].upper()
            else:
                tmp += i[n].lower()
        new_lst.append(tmp)
    
    answer = ' '.join(new_lst)
         
    return answer


print(solution('try hello world'))