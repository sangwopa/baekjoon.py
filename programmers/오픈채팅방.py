def solution(record):
    answer = []
    user_info = dict()
    tmp_info = []
    
    for i in record:
        in_info = i.split(' ')
        tmp_info.append(in_info)
        tmp = []
        str_one = ''
        str_two = ''
        if in_info[0] == 'Enter':
            if not in_info[1] in user_info.keys():
                user_info[in_info[1]] = in_info[2]
            elif in_info[2] != user_info[in_info[1]]:
                for n in range(len(answer)):
                    if tmp_info[n][1] == in_info[1]:
                        answer[n][0] = in_info[2] + '님이'                
            str_one = in_info[2] + '님이'
            str_two = '들어왔습니다.'
            tmp.append(str_one)
            tmp.append(str_two)
        elif in_info[0] == 'Leave':
            str_one = user_info[in_info[1]] + '님이'
            str_two = '나갔습니다.'
            tmp.append(str_one)
            tmp.append(str_two)    
        elif in_info[0] == 'Change':
            for n in range(len(answer)):
                if tmp_info[n][1] == in_info[1]:
                    answer[n][0] = in_info[2] + '님이'
        if not tmp == []:
            answer.append(tmp)
                
    return [' '.join(i) for i in answer]

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))