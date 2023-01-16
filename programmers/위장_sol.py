from functools import reduce

def solution(clothes):
    clth_cnt = dict()
    for i in clothes:
        if not i[1] in clth_cnt.keys():
            clth_cnt[i[1]] = 1      
        else:
            clth_cnt[i[1]] += 1
    cnt_lst = list(clth_cnt.values())
    if len(cnt_lst) == 1:
        return sum(cnt_lst)
    else:
        tmp = [i+1 for i in cnt_lst]
        return reduce(lambda x, y: x*y, tmp) - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))