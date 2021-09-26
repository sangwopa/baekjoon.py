a = input()


div = [char for char in a.upper()]

dic = {}

for i in div:
    if i in dic: 
        dic[i]+=1 # 이미 dic에 존재하면 count += 1
    else: 
        dic[i]=1 # 아니면 1로 새로 만들어 주기

dic=sorted(dic.items(), key=lambda x:x[1], reverse=True) # value값으로 정렬
        
if len(dic)>1 and dic[0][1]==dic[1][1]: 
    print('?') # 0번째 count와 1번째 count가 같으면 '?' 출력
else: 
    print(dic[0][0]) # 아니면 해당 문자 출력