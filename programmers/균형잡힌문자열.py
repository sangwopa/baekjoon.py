def solution(p):
    answer = ''
    #u에 대해
    sts = 0
    for i in p:
        if i == '(':
            sts += 1
        if i == ')':
            sts -= 1
        if sts < 0:
            break
    if sts == 0:
        return p
    else:
        splt_str(p)
        
    def recomb_str(p):
        tmp = ''
        tmp = '(' + tmp
    
    def splt_str(p):
        u = ''
        v = ''
        cnt1 = 0
        cnt2 = 0
        for i in range(len(p)):
            if p[i] == '(':
                cnt1 += 1
                u += '('
            if p[i] == ')':
                cnt2 += 1
                u += ')'        
            if cnt1 == cnt2:
                v = p[i+1:]
                break
        #u에 대해
        sts = 0
        for i in u:
            if i == '(':
                sts += 1
            if i == ')':
                sts -= 1
            if sts < 0:
                break
        if sts == 0:
            return splt_str(v)
        if sts < 0:
            return splt_str(u)

            

    
    return answer

p1 = "(()())()"
print(solution(p1))
p2 = ")("
print(solution(p2))
p3 = "()))((()"	
print(solution(p3))