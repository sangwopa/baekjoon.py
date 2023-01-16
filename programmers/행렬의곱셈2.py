import numpy as np

def solution(arr1, arr2):
    np_ar1 = np.array(arr1)
    np_ar2 = np.array(arr2)
    
    answer = np_ar1 @ np_ar2
    
    answer = answer.tolist()
    
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))