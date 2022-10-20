def solution(p):
    answer = ''
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
    def re_comb(p):
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
        