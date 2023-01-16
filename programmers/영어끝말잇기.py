def solution(n, words):
    answer = []
    wrd_lst = [words[0]]
    for i in range(1, len(words)):
        if words[i] in wrd_lst:
            if (i+1) % n == 0:
                num = n
            else:
                num = (i+1) % n
            answer.append(num)
            answer.append((i//n) + 1)
            break
        if words[i][0] != words[i-1][len(words[i-1])-1]:
            if (i+1) % n == 0:
                num = n
            else:
                num = (i+1) % n
            answer.append(num)
            answer.append((i//n) + 1)
            break 
        wrd_lst.append(words[i])
    if len(answer) == 0:
        answer = [0, 0]     
    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))

n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))