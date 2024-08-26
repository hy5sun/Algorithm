from collections import deque

N = int(input())
island_map = []
for _ in range(N):
    island_map.append(list(map(int, input().split())))
queue = deque([])
cnt = 0
dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]

for i in range(N):
    for j in range(N):
        if island_map[i][j] == 1:
            queue.append([i, j])
            island_map[i][j] = 0
            while queue:
                island = queue.popleft()
                for k in range(8):
                    x = island[0] + dx[k]
                    y = island[1] + dy[k]
                    if 0 <= x < N and 0 <= y < N:
                        if island_map[x][y] == 1:
                            queue.append([x, y])
                            island_map[x][y] = 0
            cnt += 1

print(cnt)