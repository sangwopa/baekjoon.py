num = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]] # 숫자 배열

def get_loc(x): #숫자 좌표 반환 함수
    con = []
    for i in range(len(num)):
        if x in num[i]:
            con.append(i)
            con.append(num[i].index(x))
    return con

def get_distance(x, y): #이동량 계산 함수
    con = abs(x[0]-y[0]) + abs(x[1]-y[1])
    return con

def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"
    for i in range(len(numbers)): 
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7: #왼손으로 누르는 경우
            answer = answer + "L"
            left = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9: #오른손으로 누르는 경우
            answer = answer + "R"
            right = numbers[i]
        else: 
            if get_distance(get_loc(numbers[i]), get_loc(left)) == get_distance(get_loc(numbers[i]), get_loc(right)):
            #거리가 같으면 hand에 따른 값으로 누름
                answer = answer + hand[0].upper()
                if hand == "right":
                    right = numbers[i]
                else:
                    left = numbers[i]                    
            elif get_distance(get_loc(numbers[i]), get_loc(left)) <= get_distance(get_loc(numbers[i]), get_loc(right)):
            #조건에 따라 누름
                answer = answer + "L"
                left = numbers[i]
            else:
                answer = answer + "R"
                right = numbers[i]
    return answer