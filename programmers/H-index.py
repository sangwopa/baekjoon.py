def solution(citations):
    answer = 0   
    for i in range(max(citations)+1): # 0~인용횟수의 최대값까지 검증
        cited = 0
        for n in range(len(citations)): # 해당 i 값이상이면 cited + 1
            if citations[n] >= i:
                cited += 1
        print(cited)
        if answer < i and cited >= i: # 최대값 조건과 cited가 i보다 큰 경우
            answer = i
    return answer