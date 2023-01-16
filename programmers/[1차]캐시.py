from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cities = [i.lower() for i in cities]
    set_lst = list(set(cities))
    tmp = []
    tmp = deque(tmp)
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        if not set_lst.index(i) in tmp:
            if len(tmp) == cacheSize:
                tmp.pop()
                tmp.appendleft(set_lst.index(i))
                answer += 5
            else:
                tmp.appendleft(set_lst.index(i))
                answer += 5
        else:
            tmp.remove(set_lst.index(i))
            tmp.appendleft(set_lst.index(i))      
            answer += 1
    return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize, cities))

cacheSize = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))

cacheSize = 5
["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	
print(solution(cacheSize, cities))

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))

cacheSize = 2
cities = ["a", "a", "a", "b", "b", "b", "c", "c", "c"]
print(solution(cacheSize, cities))

