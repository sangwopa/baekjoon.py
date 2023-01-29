import math

def solution(fees, records):
    answer = []
    res_dict = dict()
    records = [i.split(' ') for i in records]
    
    #차량번호: [출입 시점, 분 총합, 출입]
    #IN: 0, OUT: 1
    for i in records:
        if not i[1] in res_dict.keys() and i[2] == 'IN':
            res_dict.setdefault(i[1], [])
            res_dict[i[1]].append(i[0])
            res_dict[i[1]].append(0)
            res_dict[i[1]].append(0)
        elif i[2] == 'IN':
            res_dict[i[1]][0] = i[0]
            res_dict[i[1]][2] = 0
        else:
            res_dict[i[1]][1] += (int(i[0][:2])*60 + int(i[0][-2:])) - (int(res_dict[i[1]][0][:2])*60 + int(res_dict[i[1]][0][-2:]))
            res_dict[i[1]][2] = 1
            
    #key 기준 정렬
    res_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: item[0])}
            
    for i, e in res_dict.items():
        if e[2] == 0:
            e[1] += (23*60 + 59) - (int(e[0][:2])*60 + int(e[0][-2:]))
            
        if e[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((e[1]-fees[0])/fees[2])*fees[3])
    
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))