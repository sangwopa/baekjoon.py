#진수변환
def base_conv_expn(n, q):
    num = '0123456789ABCDEF'
    rev_base = ''
    
    if n == 0:
        return '0'

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(num[mod])

    return rev_base[::-1]

#일정 범위를 미리 계산하고 그 범위까지의 문자열 만든 뒤 추출
def solution(n, t, m, p):
    answer = ''
    length = 1
    cnt = 0
    
    while length < (m * t):
        length += (cnt + 1) * (n**(cnt+1) - n**cnt)
        cnt += 1

    
    num_lst = ''
    for i in range(n**cnt):
        num_lst += base_conv_expn(i, n)
        
    for i in range(t):
        answer += num_lst[m*i+(p-1)]
        
    return answer



# print(solution(2, 4, 2, 1))
# print(solution(2, 4, 5, 1))
# print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))