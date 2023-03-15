def solution(storey):
    answer = 0
    while storey > 0:
        storey, moves = divmod(storey, 10)
        if moves > 5 or (moves == 5 and storey % 10 >= 5):
            moves = 10 - moves
            storey += 1
        answer += moves
    return answer

print(solution(16)) # 6
print(solution(2554)) # 16
print(solution(3)) # 3
print(solution(3194)) # 10
print(solution(9000)) # 2