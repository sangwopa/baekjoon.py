from collections import deque

def room_change(str1, str2):
    time1 = str1.split(':')
    time2 = str2.split(':')
    con = (int(time2[0])*60 + int(time2[1])) - (int(time1[0])*60 + int(time1[1]) + 10)
    
    if con < 0:
        return False
    else:
        return True

def solution(book_time):
    book_time.sort(key=lambda x:x[0])
    book_time = deque(book_time)
    
    con = []
    
    while len(book_time) > 0:
        room = book_time.popleft()
        for i in con:
            if room_change(i[len(i)-1][1], room[0]):
                i.append(room)
                break
        else:
            con.append([room])

    return len(con)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))