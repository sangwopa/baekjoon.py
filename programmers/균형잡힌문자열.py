def recomb_str(p):
    u = ''
    v = ''
    sts = 0
    while 1:
        for i in p:
            if i == '(':
                u += i
                sts += 1
            if i == ')':
                u += i
                sts -= 1
            if sts < 0:
                break
            elif sts == 0:
                
            
            
            

def solution(p):
    answer = ''
    u = ''
    sts = 0
    mode = 0
    while 1:
        if mode == 0:
            for i in range(len(p)):
                if p[i] == '(':
                    u += p[i]
                    sts += 1
                if p[i] == ')':
                    u += p[i]
                    sts -= 1  
                if sts < 0:
                    answer += u
                    p = p[:i]
                    mode = -1
                    break
        else:
            for i in range(len(p)):
                if p[i] == '(':
                    u += p[i]
                    sts += 1
                if p[i] == ')':
                    u += p[i]
                    sts -= 1     
                if sts < 0:
                    answer += u
                    p = p[i:]
                    mode = -1
                    break            
            
            
            

p1 = "(()())()"
print(solution(p1))
p2 = ")("
print(solution(p2))
p3 = "()))((()"	
print(solution(p3))