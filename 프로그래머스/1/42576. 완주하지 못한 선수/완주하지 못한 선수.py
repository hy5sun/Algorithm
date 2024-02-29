def solution(participant, completion):
    dic = {}
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    
    for c in completion:
        dic[c] -= 1
        
    for name, value in dic.items():
        if value != 0:
            return name
    