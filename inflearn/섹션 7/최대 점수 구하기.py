def DFS(v, score, time):
    global max_score
    if time < 0:
        return
    if v == n and time >= 0:
        if score > max_score:
            max_score = score
        return
    else:
        DFS(v+1, score+lst[v][0], time-lst[v][1])
        DFS(v+1, score, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = []
    max_score = 0
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    DFS(0, 0, m)
    print(max_score)