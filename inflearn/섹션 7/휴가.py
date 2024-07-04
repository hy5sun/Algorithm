def DFS(v, total):
    global max_total
    if v == n:
        if max_total < total:
            max_total = total
        return
    else:
        if v + lst[v][0] <= n:
            DFS(v+lst[v][0], total + lst[v][1])
        DFS(v+1, total)

if __name__ == "__main__":
    n = int(input())
    lst = []
    max_total = 0
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    DFS(0, 0)
    print(max_total)
