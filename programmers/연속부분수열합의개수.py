def solution(elements):
    answer = []
    length = len(elements)
    elements = elements * 2
    
    for i in range(1, length+1):
        for n in range(length):
            answer.append(sum(elements[n:n+i]))           

    answer = set(answer)
    
    return len(answer)

print(solution([7,9,1,1,4]))