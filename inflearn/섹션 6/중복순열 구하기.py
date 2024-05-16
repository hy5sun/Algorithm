def DFS(i):
    global cnt
    if i > m:
        return
    if i == m:
        for r in res:
            print(r, end=' ')
        cnt += 1
        print()
    else:
        for num in range(1, n+1):
            res[i] = num
            DFS(i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
