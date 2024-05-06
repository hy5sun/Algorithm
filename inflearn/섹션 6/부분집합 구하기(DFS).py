def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1 # 사용 O
        DFS(v+1)
        ch[v] = 0 # 사용 X
        DFS(v+1)

if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1) # 원소 사용 여부 체크 변수
    DFS(1)
