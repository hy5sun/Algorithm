def DFS(v, cnt):
    if v == n+1:
        return
    if cnt == m:
        for l in lst:
            print(l, end=' ')
        print()
        return
    else:
        for i in range(1, n+1):
            if i not in lst:
                lst.append(i)
                DFS(i, cnt+1)
                lst.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = []
    DFS(0, 0)