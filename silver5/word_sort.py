N = int(input()) #단어 개수

div = [] #단어들 리스트에 저장

for i in range(N):
    div.append(input().strip())

div.sort() #단어 알파벳 순서대로, 길이 순으로 정렬
div.sort(key=len)

#똑같은 단어 삭제
index = 0
while index != N-1:
    if div[index] == div[index+1]:
        div.pop(index)
        N -= 1
        index -= 1
    index += 1
        
for i in range(len(div)):
    print(div[i])



