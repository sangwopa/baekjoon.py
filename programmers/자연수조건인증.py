from re import I


def solution(n):
    answer = n-1
    i = 2
    while(i<=(n//2)):
        con = answer
        while con != 0:
            con = con / i
            if con.is_integer() and (int(con) == 1):
                return i    
            if con.is_integer():
                continue
            if type(con)==float:
                break
        i += 1
    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
print(solution(26))
