# 함수를 조합하여 결과 출력
def rep_prg(n):
    names = [input() for _ in range(n)]
    val = [0]*n
    for i in range(2*n-1):
        a = int(input().split()[0])
        val[a-1] += 1
    for i in range(n):
        if val[i] != 2:
            index = i
            break
    con.append(names[index])
    run_prg()
    
def run_prg():
    n = int(input()) 
    if n == 0:
        return 1
    else:
        return rep_prg(n)

con = []
run_prg()

for i in range(len(con)):
    print(i+1, con[i])
    


            