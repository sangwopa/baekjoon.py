# 피보나치 수열
# n=1 일 때부터 결과를 계산해보면 피보나치라는 것을 알 수 있다.
def solution(n):
    con = {
        1: 1,
        2:2
    }
    
    if n == 1 or n == 2:
        return n
    
    for i in range(3, n+1):
        con[i] = (con[i-2] + con[i-1]) % 1000000007
    
    return con[n]
        
print(solution(4))
print(solution(7))
        
        
        