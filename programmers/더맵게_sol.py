import heapq

def solution(scoville, K):

    heapq.heapify(scoville)

    sco_num = -1 # 두 음식의 스코빌 합
    cnt = 0 # 섞는 횟수
    while scoville[0] < K:
        if len(scoville) == 1:
            cnt = -1
            break
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        sco_num = f + s*2
        heapq.heappush(scoville, sco_num)
        cnt += 1

    answer = cnt
    return answer