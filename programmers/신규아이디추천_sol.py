import re

def solution(new_id):
    st = new_id
    st = st.lower() #소문자 변환
    st = re.sub('[^a-z0-9\-_.]', '', st) #소문자, 숫자, 특수문자(-_.) 빼고 삭제
    st = re.sub('\.+', '.', st) #중복 "." 줄이기
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st