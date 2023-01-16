from math import ceil

def solution(progresses, speeds):
    answer = []
    open = []
    for i in range(len(progresses)):
        tmp = ceil((100 - progresses[i]) / speeds[i])
        open.append(tmp)
        
    stand = open[0]
    tmp = 1
    for i in range(1, len(open)):
        if i == len(open)-1:
            if open[i] <= stand:
                tmp += 1
                answer.append(tmp)
                break
            elif open[i] > stand:
                answer.append(tmp)
                answer.append(1)
                break
        if open[i] <= stand:
            tmp += 1
        elif open[i] > stand:
            answer.append(tmp)
            stand = open[i]
            tmp = 1

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))