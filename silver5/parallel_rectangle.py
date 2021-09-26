import math

div = list(map(int,input().split()))

res = []

def line_len(a, b, c, d):
    con = math.sqrt((a-c)**2+(b-d)**2)
    return con
if (div[0]-div[2])==0:
    con1 = 2*(line_len(div[2],div[3],div[4],div[5])+line_len(div[0],div[1],div[4],div[5]))
    con2 = 2*(line_len(div[0],div[1],div[2],div[3])+line_len(div[0],div[1],div[4],div[5]))
    con3 = 2*(line_len(div[0],div[1],div[2],div[3])+line_len(div[2],div[3],div[4],div[5]))
    res.append(con1)
    res.append(con2)
    res.append(con3)
    res.sort()
    print(res[2]-res[0])
elif (div[0]==0) and (div[2]==0) and (div[4]==0):
    print(float(-1))
elif (div[1]==0) and (div[3]==0) and (div[5]==0):
    print(float(-1))
elif ((div[1]-div[3])/(div[0]-div[2]))==((div[3]-div[5])/(div[2]-div[4])):
    print(float(-1))
else:
    con1 = 2*(line_len(div[2],div[3],div[4],div[5])+line_len(div[0],div[1],div[4],div[5]))
    con2 = 2*(line_len(div[0],div[1],div[2],div[3])+line_len(div[0],div[1],div[4],div[5]))
    con3 = 2*(line_len(div[0],div[1],div[2],div[3])+line_len(div[2],div[3],div[4],div[5]))
    res.append(con1)
    res.append(con2)
    res.append(con3)
    res.sort()
    print(res[2]-res[0])