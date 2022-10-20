def solution(s):
    tmp = s.split(' ')
    tmp = list(map(int, tmp))
    tmp.sort()
    return str(tmp[0]) + ' ' + str(tmp[len(tmp)-1])
s= "1 2 3 4"
print(solution(s))
s= "-1 -2 -3 -4"
print(solution(s))
s= "-1 -1"
print(solution(s))
