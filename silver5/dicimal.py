A, B, N = map(int,input().split())

cnt = 0

# 만약 A가 B보다 크거나 같다면 B보다 작게 줄이기
if A>=B:
    A = A - (A//B)*B

# 나눗셈 방식대로 N번째 소수점 자리수를 뽑아낼 때까지 반복
while cnt != N:
    con = (10*A)//B
    A = 10*A - con*B
    cnt += 1

print(con)