def solution(s):
    cnt1 = 0
    
    for i in s:
        if i == "(":
            cnt1 += 1
        else:
            cnt1 -= 1
        if cnt1 < 0:
            return False
    if cnt1 != 0:
        return False
    return True

s = "()()"	
print(solution(s))
s = "(())()"	
print(solution(s))
s = ")()("	
print(solution(s))
s = "(()("	
print(solution(s))