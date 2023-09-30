def solution(board):
    bomb = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                bomb.append([i, j])
    
    extraBomb = []
            
    for b in bomb:
        firstIdx = b[0]
        secondIdx = b[1]
        extraBomb.append((firstIdx-1, secondIdx-1))
        extraBomb.append((firstIdx-1, secondIdx))
        extraBomb.append((firstIdx-1, secondIdx+1))
        extraBomb.append((firstIdx, secondIdx-1))
        extraBomb.append((firstIdx, secondIdx))
        extraBomb.append((firstIdx, secondIdx+1))
        extraBomb.append((firstIdx+1, secondIdx-1))
        extraBomb.append((firstIdx+1, secondIdx))
        extraBomb.append((firstIdx+1, secondIdx+1))
        
    answer = extraBomb.copy()
    for eb in extraBomb:
        if eb[0] > len(board)-1 or eb[0] < 0 or eb[1] > len(board)-1 or eb[1] < 0:
            answer.remove(eb)
    
    answer = set(answer)
    
    return len(board) ** 2 - len(answer)
