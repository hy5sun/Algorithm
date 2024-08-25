from collections import deque

N, M = map(int, input().split())
maze_map = []
for _ in range(N):
    maze_map.append(list(map(int, input())))
queue = deque([[0, 0]])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = [[0] * M for _ in range(N)]
maze_map[0][0] = 0
cnt[0][0] = 1

while queue:
    player = queue.popleft()
    for i in range(4):
        x = player[0] + dx[i]
        y = player[1] + dy[i]
        if 0 <= x < N and 0 <= y < M:
            if maze_map[x][y] == 1:
                cnt[x][y] = cnt[player[0]][player[1]] + 1
                maze_map[x][y] = 0
                queue.append([x, y])

print(cnt[N-1][M-1])