from itertools import permutations, combinations

def solution(m, n, puddles):
    answer = 0
    directions = "RD"
    go = [[1, 0], [0, 1]]
    end = [i for i in 'R'*(m-1)+'D'*(n-1)]
    
    tmp = set(list(permutations(end)))
    
    for i in tmp:
        start = [1,1]
        for n in i:
            start = [x+y for x, y in zip(start, go[directions.index(n)])]
            if start in puddles:
                break
        else:
            answer += 1
        
    return answer%1000000007


print(solution(4, 3, [[2, 2]]))