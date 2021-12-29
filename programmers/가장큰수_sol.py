def solution(num): 
    num = list(map(str, num))  #리스트 원소 값 모두 str로 만들기
    num.sort(key=lambda x: x * 4, reverse=True) #1000이하의 수들이니 4자리 값으로 만들어서 비교 역순 정렬
    return str(int(''.join(num))) #0000고려하여 int로 변환후 다시 str로 변환