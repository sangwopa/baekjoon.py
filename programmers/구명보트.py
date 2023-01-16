from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    tmp = 0
    
    while len(people) > 1:
        if people [0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.popleft()
    
    if len(people) == 1:
        answer += 1
    
    return answer
            
    
            
    
    
    
    
    
    

    

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))

people = [70, 80, 50]
limit = 100
print(solution(people, limit))

people = [40, 40, 40, 70,80,80]
limit = 120
print(solution(people, limit))