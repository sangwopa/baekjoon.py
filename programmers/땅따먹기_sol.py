import copy

def hopscotch(board, size):
    result = 0
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    for i in range(1,size):
        for j in range(4):
            temp = copy.deepcopy(board[i-1])
            temp[j] = 0
            board[i][j]+=max(temp)
    result = max(board[-1])
    return result


#아래는 테스트로 출력해 보기 위한 코드입니다.
board =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
print(hopscotch(board, 3))