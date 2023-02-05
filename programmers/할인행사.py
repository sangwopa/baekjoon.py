from collections import Counter

def solution(want, number, discount):
    answer = 0
    #요구사항 딕셔너리화
    tmp_dict = {x: y for x, y in zip(want, number)}
    
    #길이 -10 만큼 동일한지 확인
    for i in range(len(discount)-9):
        cnt = dict(Counter(discount[i:10+i]))
        
        if cnt == tmp_dict:
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))