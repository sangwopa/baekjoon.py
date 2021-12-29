def solution(citations):
    citations.sort(reverse=True) #역순 정렬
    return max(map(min, enumerate(citations, start=1))) # map,min으로 h값의 집합을 뽑은 후 그 중 max 값 뽑기