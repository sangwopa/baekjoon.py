import re


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    com = re.compile('[a-z]')
    
    tmp_lst1 = []
    tmp_lst2 = []
    
    if str1 == str2:
        return 65536
    else:
        for i in range(len(str1)-1):
            if len(com.findall(str1[i]+str1[i+1])) == 2:
                tmp_lst1.append(str1[i]+str1[i+1])
            else:
                continue
            
        for i in range(len(str2)-1):
            if len(com.findall(str2[i]+str2[i+1])) == 2:
                tmp_lst2.append(str2[i]+str2[i+1])
            else:
                continue      
    
    if len(tmp_lst1) == 0 and len(tmp_lst2) == 0:
        return 65536  
    
    cpy_lst = tmp_lst1.copy()
    
    con_lst = []
    for i in range(len(cpy_lst)):
        if cpy_lst[i] in tmp_lst2:
            con_lst.append(cpy_lst[i])
            tmp_lst1.remove(cpy_lst[i])
            tmp_lst2.remove(cpy_lst[i])
                
    
    return int(((len(con_lst))/(len(tmp_lst1)+len(con_lst)+len(tmp_lst2)))*65536)


# print(solution("FRANCE", "french"))/
# print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
# print(solution("E=M*C^2", "e=m*c^2"))