def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for p in photo:
        cnt = 0
        for i in range(len(p)):
            if p[i] in dic:
                cnt += dic[p[i]]
        answer.append(cnt)
    return answer