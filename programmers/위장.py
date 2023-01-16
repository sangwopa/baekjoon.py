from functools import reduce
from itertools import combinations

def solution(clothes):
    answer = 0
    clth_cnt = dict()
    for i in clothes:
        if not i[1] in clth_cnt.keys():
            clth_cnt[i[1]] = 1      
        else:
            clth_cnt[i[1]] += 1
    cnt_lst = list(clth_cnt.values())
    
    for i in range(len(cnt_lst)):
        if i == 0:
            answer += reduce(lambda x, y: x + y, cnt_lst)
        elif i == len(cnt_lst) - 1:
            answer += reduce(lambda x, y: x * y, cnt_lst)
        else:
            con = []            
            comb = list(combinations(cnt_lst, i+1))
            for n in range(len(comb)):
                con.append(reduce(lambda x, y: x * y, comb[n]))
            answer += reduce(lambda x, y: x + y, con)

    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))