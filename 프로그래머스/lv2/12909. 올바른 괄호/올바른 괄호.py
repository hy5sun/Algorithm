def solution(s):
    count = 0
    queue = list(s)
    
    for q in queue:
        if q == "(":
            count += 1
        else:
            count -= 1
            
        if count < 0:
            return False
        
    if count == 0 and queue[0] == '(':
        return True
    else:
        return False