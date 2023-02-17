from collections import deque

def solution(bridge_length, weight, truck_weights):
    length = len(truck_weights)
    # 다리 길이가 1 혹은 트럭 대수가 1대일 때
    if bridge_length == 1 or len(truck_weights) == 1:
        return bridge_length + 1
    
    truck_weights = deque(truck_weights)
    bridge_stts = deque([[truck_weights.popleft(), 1]])
    now_weight = bridge_stts[0][0]
    con = []
    time = 1
    
    # 문제 순서대로 구현
    while len(con) < length:
        for i in bridge_stts:
            if i[1] == bridge_length + 1:
                continue
            i[1] += 1
            if i[1] == bridge_length + 1:
                tmp = i[0]
                now_weight -= tmp
                con.append(tmp)
        time += 1
        
        if len(truck_weights) == 0:
            continue

        if now_weight + truck_weights[0] <= weight:
            tmp = truck_weights.popleft()
            bridge_stts.append([tmp, 1])
            now_weight += tmp

    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
print(solution(1, 10, [10]))