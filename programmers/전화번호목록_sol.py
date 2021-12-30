def solution(phone_book):
    
    phone_book.sort(key = len) # 길이로 정렬
    phone_book.sort() # 값기준 정렬
    
    
    for i in range(len(phone_book)-1): # 정렬에 따라 붙어있는 두 수만 검증
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False        
            
    return True