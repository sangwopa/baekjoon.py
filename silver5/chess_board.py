# n(세로), m(가로) 값 및 체스판 상태 입력
n, m = map(int, input().split())
board = []
for _ in range(n): board.append(input())

val = ['WBWBWBWB', 'BWBWBWBW']

cnt = 64

for i in range(n - 7):
    for a in range(m - 7):
        val_cnt = 0
        for u in range(8):
            if u % 2 == 0:
                for b in range(8):
                    if board[i + u][a + b] != val[0][b]:
                        val_cnt += 1
            else:
                for b in range(8):
                    if board[i + u][a + b] != val[1][b]:
                        val_cnt += 1
        if cnt > val_cnt:
            cnt = val_cnt
        val_cnt = 0
        for u in range(8):
            if u % 2 == 0:
                for b in range(8):
                    if board[i + u][a + b] != val[1][b]:
                        val_cnt += 1
            else:
                for b in range(8):
                    if board[i + u][a + b] != val[0][b]:
                        val_cnt += 1
        if cnt > val_cnt:
            cnt = val_cnt
              
print(cnt)

                
            

        