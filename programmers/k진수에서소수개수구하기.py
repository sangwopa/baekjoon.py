def base_conv(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

import math

# 소수 판별 함수
def is_prime_number(x):
    if x == 1:
        return False
    
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    answer = 0
    num_str = base_conv(n, k)
    tmp = num_str.split("0")
    
    for i in tmp:
        if i != '' and is_prime_number(int(i)):
            answer += 1

    return answer

print(solution(437674, 3))
print(solution(110011, 10))