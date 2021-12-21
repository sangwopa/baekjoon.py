def solution(new_id):
    import re
    answer = new_id.lower() #소문자 변환
    specialChars = "~!@#$%^&*()=+[{]}:?,<>/" #해당 특수문자 제거
    for specialChar in specialChars:
        answer = answer.replace(specialChar, '')
    answer = re.sub('(([.])\\2{1,})', '.', answer) #중복 . 제거
    answer = answer.strip(".") #양 끝 . 제거
    if len(answer)==0: #길이가 0일경우 a로 반환
        answer = "a"
    if len(answer) >= 16: #길이 15까지 자르기
        answer = answer[:15]
    answer = answer.strip(".") #양 끝 . 없애기
    if len(answer) <= 2: #길이 3이하일 경우 반복 반환
        while len(answer) != 3:
            answer = answer + answer[len(answer)-1]
    return answer