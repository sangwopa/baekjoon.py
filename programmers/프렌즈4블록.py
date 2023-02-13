def remove_block(m, n, board):
    tmp = []
    for i in reversed(range(1, m)):
        for p in reversed(range(1, n)):
            if (board[i][p] == board[i-1][p] == board[i][p-1] == board[i-1][p-1]) and board[i][p] != 0:
                tmp.append([i, p])
                
    if len(tmp) == 0:
        return 0, board
    else:
        for i in tmp:
            board[i[0]][i[1]] = 0
            board[i[0]-1][i[1]] = 0
            board[i[0]][i[1]-1] = 0
            board[i[0]-1][i[1]-1] = 0

        return 1, board
    
def move_block(m, n, board):
    for i in range(n):
        while 1:
            for p in range(m-1):
                if board[p][i] != 0 and board[p+1][i] == 0:
                    board[p][i], board[p+1][i] = board[p+1][i], board[p][i]
                    break
            else:
                break
            
    return board

def solution(m, n, board):
    answer = 0
    board = [[i for i in n] for n in board]
    while 1:
        k, board = remove_block(m, n, board)
        if k == 0:
            break
        else:
            board = move_block(m, n, board)
            
    for i in board:
        answer += i.count(0)

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

