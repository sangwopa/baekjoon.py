# 등비수열의 합을 이용
def solution(word):
    dict = {'A' : 1, 'E' : 2, 'I' : 3, 'O': 4, 'U' : 5}
    n = len(word)
    answer = n
    for i in range(n):
        temp = 0
        for j in range(4 - i, -1, -1):
            temp += 5 ** j
        answer += temp * (dict[word[i]] - 1)
    return answer

from itertools import product

# 중복 순열 재정렬
def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1

# print(solution("A"))
# print(solution("AAA"))
print(solution("AAAAE"))
print(solution("AAAE"))
# print(solution("AAEU"))
# print(solution("AAE"))
# print(solution("AEU"))
# print(solution("E"))
# print(solution("EA"))
print(solution("I"))
print(solution("EIO"))