def solution(d, budget):
    d.sort()
    answer = 0
    sumD = 0
    for dd in d:
        if sumD + dd > budget:
            break
        sumD += dd
        answer += 1
    return answer