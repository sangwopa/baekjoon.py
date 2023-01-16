def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = [0 for n in range(len(arr1[0]))]
        for n in range(len(arr2[0])):
            num = 0
            for p in range(len(arr1[0])):
                num += arr1[i][p] * arr2[p][n]
            tmp[n] = num 
           
        answer.append(tmp)

    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))