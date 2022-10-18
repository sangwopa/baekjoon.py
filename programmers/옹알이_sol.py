def solution(babbling):
    tmp = ["aya", "ye", "woo", "ma"]
    tmp_except = ["ayaaya", "yeye", "woowoo", "mama"]
    
    answer = 0
    for i in babbling:
        for n in tmp:
            if n*2 not in i:
                i = i.replace(n, ' ')
        i = i.strip()
        print("i: ", i)
        if len(i) == 0:
            answer += 1

    return answer

div = ["aya", "yee", "u", "maa"]       
print(solution(div))
div = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa", "woowo"]
print(solution(div))