def solution(sizes):
    w, h = 0, 0    
    for i in sizes:
        tmp = sorted(i, reverse=True)
        if w < tmp[0]:
            w = tmp[0]
        if h < tmp[1]:
            h = tmp[1]
    answer = w * h
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]	
print(solution(sizes))

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))