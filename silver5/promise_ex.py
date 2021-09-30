N = int(input())

con = []

# 리스트에 약속시간과 도착시간의 차를 저장
for i in range(N):
    a, b = map(int, input().split())
    con.append(a-b)

# 오름 차순 정렬
con.sort()

# 홀수일 때는 중간값이 1개여서 T의 개수는 1개 짝수일 떄는 중간값 사이의 모든 정수가 T값(회귀 분석)
if N%2==1:
    print(1)
else:
    print(con[int(N/2)]-con[int(N/2)-1]+1)