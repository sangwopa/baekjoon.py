a = str(input())

con = []

# 26개의 리스트 
for i in range(26):
    con.append(0)

# 알파벳 인식시 리스트 변수 +1
for i in range(len(a)):
    if a[i] == 'a' or a[i] =='A':
        con[0] += 1
    elif a[i] == 'b' or a[i] =='B':
        con[1] += 1
    elif a[i] == 'c' or a[i] =='C':
        con[2] += 1
    elif a[i] == 'd' or a[i] =='D':
        con[3] += 1
    elif a[i] == 'e' or a[i] =='E':
        con[4] += 1
    elif a[i] == 'f' or a[i] =='F':
        con[5] += 1
    elif a[i] == 'g' or a[i] =='G':
        con[6] += 1
    elif a[i] == 'h' or a[i] =='H':
        con[7] += 1
    elif a[i] == 'i' or a[i] =='I':
        con[8] += 1
    elif a[i] == 'j' or a[i] =='J':
        con[9] += 1
    elif a[i] == 'k' or a[i] =='K':
        con[10] += 1
    elif a[i] == 'l' or a[i] =='L':
        con[11] += 1
    elif a[i] == 'm' or a[i] =='M':
        con[12] += 1
    elif a[i] == 'n' or a[i] =='N':
        con[13] += 1
    elif a[i] == 'o' or a[i] =='O':
        con[14] += 1
    elif a[i] == 'p' or a[i] =='P':
        con[15] += 1
    elif a[i] == 'q' or a[i] =='Q':
        con[16] += 1
    elif a[i] == 'r' or a[i] =='R':
        con[17] += 1
    elif a[i] == 's' or a[i] =='S':
        con[18] += 1
    elif a[i] == 't' or a[i] =='t':
        con[19] += 1
    elif a[i] == 'u' or a[i] =='U':
        con[20] += 1
    elif a[i] == 'v' or a[i] =='V':
        con[21] += 1
    elif a[i] == 'w' or a[i] =='W':
        con[22] += 1
    elif a[i] == 'x' or a[i] =='X':
        con[23] += 1
    elif a[i] == 'y' or a[i] =='Y':
        con[24] += 1
    elif a[i] == 'z' or a[i] =='Z':
        con[25] += 1
    else:
        break


# 조건 적용
max = 0
alpha = 0
cnt = 0 

for i in range(len(con)):
    if con[i] > max:
        max = con[i]
        alpha = i

for i in range(len(con)):
    if con[i] == max:
        cnt += 1

if cnt >= 2:
    print("?")
else:
    if alpha == 0:
        print('A')
    elif alpha == 1:
        print('B')
    elif alpha == 2:
        print('C')
    elif alpha == 3:
        print('D')
    elif alpha == 4:
        print('E')
    elif alpha == 5:
        print('F')
    elif alpha == 6:
        print('G')
    elif alpha == 7:
        print('H')
    elif alpha == 8:
        print('I')
    elif alpha == 9:
        print('J')
    elif alpha == 10:
        print('K')
    elif alpha == 11:
        print('L')
    elif alpha == 12:
        print('M')
    elif alpha == 13:
        print('N')
    elif alpha == 14:
        print('O')
    elif alpha == 15:
        print('P')
    elif alpha == 16:
        print('Q')
    elif alpha == 17:
        print('R')
    elif alpha == 18:
        print('S')
    elif alpha == 19:
        print('T')
    elif alpha == 20:
        print('U')
    elif alpha == 21:
        print('V')
    elif alpha == 22:
        print('W')
    elif alpha == 23:
        print('X')
    elif alpha == 24:
        print('Y')
    else:
        print('Z')