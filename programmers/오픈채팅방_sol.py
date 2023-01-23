from collections import defaultdict

def solution(record):
    answer = []
    # 1. 레코드를 분할해서 id참조 가능한 리스트를 만든다
    _record = [i.split(" ") for i in record]
    
    seen = set()
    hash_map = defaultdict(list)
    
    for i in reversed(range(len(_record))):
        if _record[i][0] == 'Change' or _record[i][0] == 'Enter':
            if not _record[i][1] in seen:
                seen.add(_record[i][1])
                hash_map[_record[i][1]] = _record[i][2]
    
    result_record = [i for i in _record if i[0] == 'Enter' or i[0] == 'Leave']
        
    tmp_msg = {
        'Enter': '들어왔습니다.',
        'Leave': '나갔습니다.'
        }
    
    for i in range(len(result_record)):
        answer.append(f'{hash_map[result_record[i][1]]}님이 {tmp_msg[result_record[i][0]]}')
    
    return answer
    
    
    
    
    
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))