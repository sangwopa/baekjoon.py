def solution(arr):
    answer = []
    n = 0
    for n in range(len(arr)):
        if n == (len(arr) - 1):
            answer.append(arr[n])
            break
        if arr[n] == arr[n+1]:
            n += 1
            continue
        if arr[n] != arr[n+1]:
            answer.append(arr[n])
            n += 1
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))
arr = [4,4,4,3,3]
print(solution(arr))
        