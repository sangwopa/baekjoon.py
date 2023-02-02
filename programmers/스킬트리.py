def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        seq = 0
        stts = 0
        for n in i:
            if n in skill and skill[seq] != n:
                stts = 1
                break
            if n in skill and skill[seq] == n:
                seq += 1
                continue
        if seq == len(skill) or stts == 0:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))