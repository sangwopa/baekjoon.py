N, S, P = map(int, input().split())

if N == 0: # EOF 고려를 위한 처리
    con = []
else:
    con = list(map(int,input().split()))

# 리스트에 새 점수를 붙인 후 내림차순 정렬
con.append(S)
con.sort(reverse=True)

# 리스트에 새 점수가 있는지 확인하여 카운트
cnt = 0
for i in range(len(con)):
    if S == con[i]:
        ran = i
        cnt += 1

# 새 점수가 범위를 넘어서면, 똑같은 점수가 있을 경우를 고려하여 출력
if ran+1 > P:
    print(-1)
elif cnt > 1:
    print(ran-(cnt-2))
else:
    print(ran+1)






