t = int(input())
div = list(map(int,input().split()))
n = int(input()) # 데이터 받아오기

div.sort() # 리스트 오름차순 정렬
cnt  = 0 # 카운트

# 구간에서 순서를 고려하여 2개의 숫자 뽑기
def permutation(a, b):
    con = []
    temp = []
    for i in range(b - a):
        for u in range(b - a - i):
            temp = [a + i, a + i + u + 1]
            con.append(temp)
    return con

if len(div) == 1:
    res = []
    res = permutation(1, div[0] - 1)
    for u in range(len(res)):
        if (n >= res[u][0]) & (n <= res[u][1]):
            cnt += 1
else:
    # 해당되는 구간을 찾고, 구간안에서 카운트
    res = []
    for i in range(t - 1):
        if (n > div[i]) & (n < div[i + 1]):
            res = permutation(div[i] + 1, div[i + 1] - 1)
            for u in range(len(res)):
                if (n >= res[u][0]) & (n <= res[u][1]):
                    cnt += 1

print(cnt)




