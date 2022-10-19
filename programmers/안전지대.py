def solution(board):
    answer = 0
    lenghth = len(board)
    for i in range(lenghth):
        for n in range(lenghth):
            if board[i][n]==1:
                for u in range(-1, 2):
                    for p in range(-1, 2):
                        if (u == 0) and (p == 0):
                            continue
                        if ((i+u) < 0) or ((i+u)  >= lenghth) or ((n+p) < 0) or ((n+p)  >= lenghth):
                            continue
                        if board[i+u][n+p] == 1:
                            continue
                        else:
                            board[i+u][n+p] = 'x'
    for i in range(lenghth):
        for n in range(lenghth):
            if board[i][n]==0:
                answer += 1        
 
    return answer

board1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board1))
board2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
print(solution(board2))
board3 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
print(solution(board3))
board4 = [[0, 0], [0, 1]]
print(solution(board4))