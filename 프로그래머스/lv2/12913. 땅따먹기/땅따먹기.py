def solution(land): 
    answer = 0 
    for i in range(len(land) -1):
        max_num = max(land[i]) 
        idx = land[i].index(max(land[i])) 
        land[i].pop(idx)
        num = max(land[i])  
        for k in range(4):
            if k == idx: 
                land[i+1][k] += num  
            else: 
                land[i+1][k] += max_num 
    return max(land[-1])