def Wchess_board(a, b):
    Wcon = []
    
    for i in range(a):
        temp = []
        if i % 2 == 0:
            for n in range(b):
                if n % 2 == 0:
                    temp.append('W')
                else:
                    temp.append('B')
            Wcon.append(temp)
        else:
            for n in range(b):
                if n % 2 == 0:
                    temp.append('B')
                else:
                    temp.append('W')
            Wcon.append(temp)

    return Wcon

def Bchess_board(a, b):
    Bcon = []
    
    for i in range(a):
        temp = []
        if i % 2 == 1:
            for n in range(b):
                if n % 2 == 0:
                    temp.append('W')
                else:
                    temp.append('B')
            Bcon.append(temp)
        else:
            for n in range(b):
                if n % 2 == 0:
                    temp.append('B')
                else:
                    temp.append('W')
            Bcon.append(temp)

    return Bcon

n, m = map(int, input().split())

con = []

for i in range(n):
    temp = []
    for n in range(m):
        a = str(input())
        temp.append(a)
    con.append(temp)

num1 = 0
num2 = 0

Wcon = Wchess_board(n ,m)
Bcon = Bchess_board(n, m)

for i in range(n):
    for n in range(m):
        if con[n][m] == Wcon[n][m]:
            continue
        else:
            num1 += 1

for i in range(n):
    for n in range(m):
        if con[n][m] == Bcon[n][m]:
            continue
        else:
            num2 += 1

if num1 >= num2:
    print(num1)
else:
    print(num2)
