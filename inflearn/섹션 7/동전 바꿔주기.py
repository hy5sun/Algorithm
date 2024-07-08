def DFS(v, total):
    global cnt
    if total == t:
        cnt += 1
        return
    if v == k or total > t:
        return
    else:
        for i in range(lst[v][1]+1):
            DFS(v+1, total + lst[v][0] * i)

if __name__ == "__main__":
    t = int(input())
    k = int(input())
    lst = []
    cnt = 0
    for _ in range(k):
        p, n = map(int, input().split())
        lst.append([p, n])
    DFS(0, 0)
    print(cnt)
