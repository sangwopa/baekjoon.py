# 문제 잘못 이해함
# 만약 전체를 고려해 다음 큰수를 append하는거라면 정답
def solution(numbers):
    answer = []
    tmp_numbers = numbers.copy()
    numbers.sort()
    max_num = numbers[len(numbers)-1]
    
    for i in range(len(tmp_numbers)):
        idx = numbers.index(tmp_numbers[i])+1
        if tmp_numbers[i] == max_num:
            answer.append(-1)
            continue
        
        while 1:
            if numbers[idx] <= tmp_numbers[i]:
                idx += 1
            else:
                answer.append(numbers[idx])
                break
                
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))            
        