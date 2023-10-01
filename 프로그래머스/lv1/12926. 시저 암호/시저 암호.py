def solution(s, n):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V', 'W', 'X', 'Y', 'Z']
    answer = ''
    for ss in s:
        if ss == ' ':
            answer += ss
            continue
        
        idx = alpha.index(ss.upper()) + n
        if idx >= len(alpha):
            idx -= len(alpha)
        
        if ss != ss.upper():
            ss = ss.upper()
            answer += alpha[idx].lower()
        else:
            answer += alpha[idx]
            
    return answer