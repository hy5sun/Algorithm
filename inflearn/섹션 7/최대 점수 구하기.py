def DFS(v, score, time):
    global max_score
    if time < 0:
        return
    last_score = sum(a[0] for a in lst[v:])
    if score + last_score < max_score:
        return
    if v == n-1 and time >= 0:
        if score > max_score:
            max_score = score
        return
    else:
        DFS(v+1, score+lst[v+1][0], time-lst[v+1][1])
        DFS(v+1, score, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = []
    max_score = 0
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    lst.sort(reverse=True)
    DFS(-1, 0, m)
    print(max_score)