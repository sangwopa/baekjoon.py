
def cal_slope(tmp1, tmp2):
    return (tmp1[1]-tmp2[1])/(tmp1[0]-tmp2[0])

def solution(dots):
    case_list = [[0,1,2,3], [0,2,1,3], [0,3,1,2]]
    
    for i in case_list:
        if cal_slope(dots[i[0]], dots[i[1]]) == cal_slope(dots[i[2]], dots[i[3]]):
            return 1
    return 0

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots))

dots = [[3, 5], [4, 1], [2, 4], [5, 10]]
print(solution(dots))