def solution(a, b, n):
    con = 0
    while 1:
        get_coke = (n // a) * b
        else_bottle = n % a
        con += get_coke
        n = get_coke + else_bottle
        if n < a:
            break
    
    return con

print(solution(2, 1, 20))
print(solution(3, 1, 20))

        
        

