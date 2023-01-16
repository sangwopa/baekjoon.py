def solution(numbers, target):
    answer = 0
    nodes = [0]
    if sum(numbers) < target:
        return 0
    elif sum(numbers) == target:
        return 1
    else:
        for i in numbers:
            tmp = []
            for n in nodes:
                tmp.append(n + i)
                tmp.append(n - i)
            nodes = tmp
        for i in nodes:
            if i == target:
                answer += 1
        return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))