from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    num_case = list(permutations(numbers)) #n!의 경우의 수 모두를 고려해 최대값 찾기
    div = []
    for i in range(len(num_case)):
        div.append(''.join(num_case[i]))
    return max(div)