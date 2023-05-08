def solution(n):
    answer = 1
    
    for i in range(1, n):
        summ = i
        while(summ < n):
            i += 1
            summ += i
            if summ == n:
                answer += 1
    
    return answer