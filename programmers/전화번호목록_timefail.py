def solution(phone_book):
    answer = True
    for i in phone_book:
        count = 0
        for n in phone_book:
            if len(n) >= len(i):
                temp = n[0:len(i)]
                if temp == i and count >= 1:
                    return False
                if temp == i:
                    count += 1
    return answer