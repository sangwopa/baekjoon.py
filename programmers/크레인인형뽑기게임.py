def solution(board, moves):
    answer = 0
    temp = []
    for i in range(len(moves)):
        for n in range(len(board)): #보드에서 0이 아닌 수를 찾아 temp에 append
            if board[n][moves[i]-1] != 0:
                temp.append(board[n][moves[i]-1])
                board[n][moves[i]-1] = 0
                break
        if len(temp) >= 2: #길이가 2이상일때 뒤에 두개가 같으면 뒤에 두개 삭제
            if temp[len(temp)-1] == temp[len(temp)-2]:
                temp.pop()
                temp.pop()
                answer += 2 #조건 만족할때마다 2더해주기
    return answer