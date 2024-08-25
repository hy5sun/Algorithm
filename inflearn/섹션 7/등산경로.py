def climbing(x, y):
    global cnt
    if mountain[x][y] == dst:
        cnt += 1
        return
    else:
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if ch[next_x][next_y] == 0 and mountain[next_x][next_y] > mountain[x][y]:
                    ch[next_x][next_y] = 1
                    climbing(next_x, next_y)
                    ch[next_x][next_y] = 0


if __name__ == "__main__":
    N = int(input())
    mountain = []
    start = 1000000
    dst = 0
    for _ in range(N):
        h = list(map(int, input().split()))
        start = min(start, min(h))
        dst = max(dst, max(h))
        mountain.append(h)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        if start in mountain[i]:
            start = [i, mountain[i].index(start)]
            break
    cnt = 0
    ch = [[0] * N for _ in range(N)]
    ch[start[0]][start[1]] = 1
    climbing(start[0], start[1])
    print(cnt)
