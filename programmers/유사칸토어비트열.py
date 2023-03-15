# 시간초과
def get_cantor(n):
    cantor = ['1']
    
    for i in range(0, n):
        tmp = []
        for n in range(len(cantor)):
            if cantor[n] == '0':
                tmp.extend(['0', '0', '0', '0', '0'])
            else:
                tmp.extend(['1', '1', '0', '1', '1'])
        
        cantor = tmp.copy()      
    
    return ''.join(cantor)

def solution(n, l, r):
    tmp = get_cantor(n)

    return tmp[l-1:r].count('1')

print(solution(2, 4, 17))