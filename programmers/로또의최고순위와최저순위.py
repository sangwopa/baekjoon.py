def solution(lottos, win_nums):
    answer = []
    min_num = 0
    max_num = lottos.count(0) #0개수 세기
    for i in lottos: #최소 당첨 경우
        if i in win_nums:
            min_num = min_num + 1
    max_num = max_num + min_num #최대 당첨 경우
    if max_num == 6: #순위 저장
        con1 = 1
    elif max_num == 5:
        con1 = 2
    elif max_num == 4:
        con1 = 3
    elif max_num == 3:
        con1 = 4
    elif max_num == 2:
        con1 = 5
    else:
        con1 = 6
    if min_num == 6:
        con2 = 1
    elif min_num == 5:
        con2 = 2
    elif min_num == 4:
        con2 = 3
    elif min_num == 3:
        con2 = 4
    elif min_num == 2:
        con2 = 5
    else:
        con2 = 6
    answer.append(con1)
    answer.append(con2)                
    return answer