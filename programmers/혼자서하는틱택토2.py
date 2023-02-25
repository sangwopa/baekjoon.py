# 비정상적인 경우
# 승부가 안 났을 때
# X가 O보다 많을 때
# 승부가 났을 때
# 이겼을때 돌 숫자 판별
# 이겼을때 겹치는 경우 고려
def solution(board):
    o_cnt, x_cnt = 0, 0
    stts = 0
    o_win_cnt = 0
    x_win_cnt = 0
    
    # 누가 이겼는지 1: O, 2: X
    who_win = 0
    
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] == 'O' or board[i][0] == 'X'):
            if stts == 0:
                stts = 1
                if board[i][0] == 'O':
                    who_win = 1
                else:
                    who_win = 2
            if board[i][0] == 'O':
                o_win_cnt += 1
            else:
                x_win_cnt += 1  
                
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] == 'O' or board[0][i] == 'X'):
            if stts == 0:
                stts = 1
                if board[0][i] == 'O':
                    who_win = 1
                else:
                    who_win = 2
            if board[0][i] == 'O':
                o_win_cnt += 1
            else:
                x_win_cnt += 1  
                            
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] == 'O' or board[0][0] == 'X'):
        if stts == 0:
            stts = 1
            if board[0][0] == 'O':
                who_win = 1
            else:
                who_win = 2
        if board[0][0] == 'O':
            o_win_cnt += 1
        else:
            x_win_cnt += 1    
                  
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] == 'O' or board[0][2] == 'X'):
        if stts == 0:
            stts = 1
            if board[0][2] == 'O':
                who_win = 1
            else:
                who_win = 2
        if board[0][2] == 'O':
            o_win_cnt += 1
        else:
            x_win_cnt += 1   
               
    for i in board:
        o_cnt += i.count('O')
        x_cnt += i.count('X')
        
    # X가 O보다 많을 때, 차이가 2이상 날때
    if x_cnt > o_cnt or abs(o_cnt-x_cnt) >= 2:
        return 0     
    
    # 승부가 났을 때
    if who_win == 1:
        if x_cnt == o_cnt:
            return 0
    elif who_win == 2:
        if o_cnt > x_cnt:
            return 0
        
    if o_win_cnt == 2 and o_cnt == 5 and x_cnt == 4:
        return 1

    if o_win_cnt + x_win_cnt >= 2:
        return 0

    return 1


# print(solution(["O.X", ".O.", "..X"])) # 1
# print(solution(["OOO", "...", "XXX"])) # 0
# print(solution(["...", ".X.", "..."])) # 0
# print(solution(["...", "...", "..."])) # 1
# print(solution(["XO.", "OXO", "XOX"])) # 1
print(solution(["OOO", "XOX", "XXO"])) # 1
print(solution(["OOO", "O..", "XXX"])) # 0
print(solution(["XXX", "...", "OOO"])) # 0