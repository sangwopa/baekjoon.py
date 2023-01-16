from collections import deque, Counter

def solution(s):
    answer = 0
    left_side = "[({"
    right_side = "])}"
    
    for i in range(len(s)):
        stts = [0, 0, 0]
        seq = deque([])
        for n in range(len(s)):
            if s[n] in left_side:
                stts[left_side.index(s[n])] += 1
                seq.append(left_side.index(s[n]))
            if s[n] in right_side:
                stts[right_side.index(s[n])] -= 1
                if -1 in stts:
                    break                
                if seq.pop() != right_side.index(s[n]):
                    break
            if not True in stts and n == len(s) - 1:
                answer += 1
                break
        tmp = deque(s)
        tmp_str = tmp.popleft()
        tmp.append(tmp_str)
        s = ''.join(tmp)

    return answer

s = "[](){}"
print(solution(s))

s = "}]()[{"
print(solution(s))

s = "[)(]"
print(solution(s))

s = "}}}"
print(solution(s))

s = "]"
print(solution(s))

s = "[{]}"
print(solution(s))


