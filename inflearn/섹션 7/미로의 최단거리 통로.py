from collections import deque
import sys

maze_map = []
for _ in range(7):
    maze = list(map(int, input().split()))
    maze_map.append(maze)
queue = deque([[0, 0]])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = [[0] * 7 for _ in range(7)]

while queue:
    player = queue.popleft()
    if player == [6, 6]:
        print(cnt[6][6])
        sys.exit()
    for i in range(4):
        x = player[0] + dx[i]
        y = player[1] + dy[i]
        if 0 <= x < 7 and 0 <= y < 7 and maze_map[x][y] == 0:
            maze_map[x][y] = 1
            cnt[x][y] = cnt[player[0]][player[1]] + 1
            queue.append([x, y])

print(-1)