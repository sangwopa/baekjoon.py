a = int(input())

stk = [64]

# 리스트에 조건에 맞게 나눠진 숫자가 들어가게 하는 재귀 함수 지금 생각해보니 이진법으로 풀면 될듯;;
def cut_stk(stk, a):
    b = int(stk[len(stk)-1]/2)
    stk.pop(len(stk)-1)
    stk.append(b)
    sum = 0
    for i in range(len(stk)):
        sum+=i
    if sum > a:
        return cut_stk(stk, a)
    elif sum < a:
        stk.append(b)
    else:
        print(len(stk))    

# a가 64이면 1출력 나머지는 재귀함수 실행
if a == 64:
    print(1)
else:
    cut_stk(stk, a)

