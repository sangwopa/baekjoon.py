def solution(participant, completion):
    d = dict() # 딕셔너리
    for i in participant:
        d[i] = d.get(i, 0) + 1 # 각 항목에 0을 넣고 +1 중복일 경우 더해지도록
    for i in completion: # completion에 있는 항목들 -1
        d[i] -= 1
        if d[i] == 0: # 값이 0이라면 삭제
            del(d[i])
    return list(d.keys()).pop() # 남은 key 반환