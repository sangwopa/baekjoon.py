import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) # 목록개수세어서 dict로 치환후 빼기
    return list(answer.keys())[0]