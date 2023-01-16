def solution(triangle):
    tmp = dict()
    tmp_seq = dict()
    for i in range(len(triangle)):
        if i == 0:
            tmp[i+1] = [triangle[0][0]]
            tmp_seq[i+1] = [0]
        else:
            tmp[i+1] = []
            tmp_seq[i+1] = []
    
    for i in range(len(triangle)):
        if i == 0:
            continue
        else:
            for n in range(len(tmp[i])):
                tmp[i+1].append(tmp[i][n] + triangle[i][tmp_seq[i][n]])
                tmp_seq[i+1].append(tmp_seq[i][n])
                tmp[i+1].append(tmp[i][n] + triangle[i][tmp_seq[i][n]+1])
                tmp_seq[i+1].append(tmp_seq[i][n]+1)               

    return max(tmp[len(triangle)])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
print(solution(triangle))