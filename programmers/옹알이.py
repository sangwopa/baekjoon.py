def solution(babbling):
    tmp = ["ye", "ma", "aya",  "woo"]
    answer = 0
    for i in babbling:
        print("i: ", i)
        lst = tmp.copy()
        while 1:
            for n in lst:
                if len(n) > len(i):
                    break
                if n == i[:len(n)]:
                    i = i[len(n):]
                    lst.remove(n)
                    lst.sort(key=len)
                    break
            if len(i) == 0:
                answer += 1
                print("true")
                break     
            cnt=0
            for n in lst:
                if n in i:
                    break
                cnt += 1
            if cnt == len(lst):
                break
    return answer

div = ["aya", "yee", "u", "maa"]       
print(solution(div))
div = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa", "woowo"]
print(solution(div))