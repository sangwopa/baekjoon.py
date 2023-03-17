# 쿼드 트리
def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    # 모든 원소 같은 경우 검증
    if sum([sum(i) for i in arr]) == (length**2):
        return [0, 1]
    
    if sum([sum(i) for i in arr]) == 0:
        return [1, 0]
    
    # 크기 반으로 나눠가며 전체 탐색
    length //= 2
    while length > 1:
        for i in range(len(arr)//length):
            for n in range(len(arr)//length):
                if arr[i*length][n*length] == 'X':
                    continue
                
                # 할당 크기 원소가 모두 같을 경우 검증
                val = 0
                for k in arr[i*length:i*length+length]:
                    val += sum(k[n*length:n*length+length])
                
                # 모두 같은 경우 해당 부분 'X'로 치환
                if val == length**2:
                    answer[1] += 1
                    for k in arr[i*length:i*length+length]:
                        k[n*length:n*length+length] = ['X' for _ in k[n*length:n*length+length]]                     
                elif val == 0:
                    answer[0] += 1  
                    for k in arr[i*length:i*length+length]:
                        k[n*length:n*length+length] = ['X' for _ in k[n*length:n*length+length]]      
        length //= 2     
    
    # 나머지 원소 개수 카운트
    for i in arr:
        for n in i:
            if n == 0:
                answer[0] += 1
            elif n == 1:
                answer[1] += 1              

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))