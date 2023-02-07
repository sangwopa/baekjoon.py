from collections import deque

def solution(begin, target, words):
    # target이 words에 없을 경우 결과는 낼 수 없음
    if not target in words:
        return 0
    
    tmp = deque([[begin, 0]])
    
    while tmp:
        tmp_word, cnt = tmp.popleft()
        
        if tmp_word == target:
            return cnt
        
        for i in range(len(words)):
            diff = 0
            # 집합으로도 생각했으나 뒤집혔을때의 반례가 있기 때문에 아래와 같이 검증
            for n in range(len(tmp_word)):
                if tmp_word[n] != words[i][n]:
                    diff += 1
            
            if diff == 1:
                tmp.append([words[i], cnt+1])
    
    #모든 경우를 찾아봤으나 결과와 일치하지 않았을 경우
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
        