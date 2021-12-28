def solution(array, commands):
    answer = []
    for i in range(len(commands)): 
        div = array[commands[i][0]-1:commands[i][1]] #범위 리스트 임시 지정
        div.sort() #리스트 정렬
        answer.append(div[commands[i][2]-1]) #결과 append
    
    return answer