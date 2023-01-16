from itertools import combinations
from math import modf

def cal_com(a, b):
    tmp = (a[0]*b[1]-a[1]*b[0])
    if tmp == 0:
        return "par"
    x = (a[1]*b[2]-a[2]*b[1])/(a[0]*b[1]-a[1]*b[0])
    y = (a[2]*b[0]-a[0]*b[2])/(a[0]*b[1]-a[1]*b[0])
    x_pr = modf(x)
    y_pr = modf(y)
    if x_pr[0] != 0.0 or y_pr[0] != 0.0:
        return "flt"
    return [int(x), int(y)]

def solution(line):
    answer = []
    comb = combinations([i for i in range(len(line))], 2)
    tmp = []
    min_x = 500
    min_y = 500
    max_x = -500
    max_y = -500
    for i in comb:
        con = cal_com(line[i[0]], line[i[1]])
        if type(con)== list:
            tmp.append(cal_com(line[i[0]], line[i[1]]))
            if con[0] <= min_x:
                min_x = con[0]
            if con[0] >= max_x:
                max_x = con[0]                
            if con[1] <= min_y:
                min_y = con[1]                
            if con[1] >= max_y:
                max_y = con[1]                
        else:
            continue
    
    for i in range(max_y, min_y-1, -1):
        star = ''
        for n in range(max_x, min_x-1, -1):
            if [n, i] in tmp:
                star += '*'
            else:
                star += '.'
        answer.append(star)

    return answer

line = [[2, -1, 4], [-2, -1, 4],[0, -1, 1], [5, -8, -12],[5, 8, 12]]
print(solution(line))

line = [[0, 1, -1], [1, 0, -1],[1, 0, 1]]
print(solution(line))

line = [[1, -1, 0], [2, -1, 0]]
print(solution(line))

line = [[1, -1, 0], [2, -1, 0],[4, -1, 0]]
print(solution(line))