from itertools import permutations

def solution(k, dungeons):
    answer = -1
    length = len(dungeons)
    seq = [i for i in range(length)]
    perm = list(permutations(seq, length))
    
    for i in perm:
        if answer == length:
            break
        stts = 0
        exhuasted = k
        for n in i:
            if dungeons[n][0] > exhuasted:
                break
            else:
                exhuasted -= dungeons[n][1]
                stts += 1
            
        if answer < stts:
            answer = stts

    return answer



print(solution(80, [[80,20],[50,40],[30,10]]))