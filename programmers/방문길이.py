def solution(dirs):
    answer = 0
    directions = "UDRL"
    move = [[0,1], [0,-1], [1,0], [-1,0]]
    now = [0, 0]
    discovered = []
    
    for i in dirs:
        moved = [x + y for x, y in zip(now, move[directions.index(i)])]
        tmp = [now, moved]
        now = moved
        if tmp in discovered or tmp[::-1] in discovered:
            continue    
        if moved[0] == 6:
            moved[0] = 5
            now = moved
            continue
        elif moved[0] == -6:
            moved[0] = -5
            now = moved
            continue
        elif moved[1] == 6:
            moved[1] = 5
            now = moved
            continue 
        elif moved[1] == -6:     
            moved[1] = -5
            now = moved
            continue             
        discovered.append(tmp)

        answer += 1
        now = moved

    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))