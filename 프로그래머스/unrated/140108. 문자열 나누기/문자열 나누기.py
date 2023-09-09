def solution(s):
    answer = diff = 0
    same = 1
    i = 1
    while i < len(s):
        if s[0] == s[i]:
            same += 1
        else:
            diff += 1
        if same == diff:
            answer += 1
            s = s[i+1:]
            diff = i = 0
            same = 1
        i += 1
    if len(s) != 0:
        answer += 1
    return answer