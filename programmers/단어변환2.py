from itertools import permutations

def solution(begin, target, words):
    answer = 51
    length = len(begin)
    
    # 가능한 탐색 경로 모든 경우의 수
    perm = permutations(range(len(words)), len(words))
    
    if not target in words:
        return 0
    
    for i in list(perm):
        tmp = begin
        cnt = 0
        stts = 0
        for n in i:
            # 교집합 길이가 1일때 진행
            if len(set(tmp) & set(words[n])) == (length - 1):
                cnt += 1
                tmp = words[n]
                if tmp == target:
                    stts = 1
                    break
                else:
                    continue
            else:
                continue
        if stts == 1 and answer > stts:
            answer = cnt

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))