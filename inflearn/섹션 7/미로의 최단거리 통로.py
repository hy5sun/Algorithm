from collections import deque
import sys

maze_map = []
for _ in range(7):
    maze = list(map(int, input().split()))
    maze_map.append(maze)
queue = deque([[0, 0, 0]])
ch = [[0] * 7 for _ in range(7)]

while queue:
    player = queue.popleft()
    if player[0] == 6 and player[1] == 6:
        print(player[2])
        sys.exit()
    if 0 <= player[0] < 7 and 0 <= player[1] < 7:
        if maze_map[player[0]][player[1]] == 0 and ch[player[0]][player[1]] == 0:
                ch[player[0]][player[1]] = 1
                queue.append([player[0]+1, player[1], player[2]+1])
                queue.append([player[0], player[1]+1, player[2]+1])
                queue.append([player[0]-1, player[1], player[2]+1])
                queue.append([player[0], player[1]-1, player[2]+1])

print(-1)