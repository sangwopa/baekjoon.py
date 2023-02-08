def solution(m, n, puddles):
    # 가는 길 위, 아래 경우의 수를 더하면 그 지점의 경우의 수가 나오는 방법
    # 연산을 위해 한 겹 씌워줌
    table = [[0] * (m + 1) for _ in range(n + 1)]
    table[1][1] = 1
    
    # 물 웅덩이 인식
    for i in puddles:
        table[i[1]][i[0]] = -1

        
    for i in range(1, n + 1):
        for p in range(1, m + 1):
            if table[i][p] == -1:
                table[i][p] = 0
                continue
            
            table[i][p] += (table[i-1][p] + table[i][p-1]) % 1000000007

    return table[n][m]


print(solution(4, 3, [[2, 2]]))