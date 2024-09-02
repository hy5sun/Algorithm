from collections import deque
import copy

N = int(input())
areas = []
lowest = 100
highest = 0
for _ in range(N):
    area = list(map(int, input().split()))
    lowest = min(lowest, min(area))
    highest = max(highest, max(area))
    areas.append(area)
tmp = copy.deepcopy(areas)
queue = deque([])
answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for w in range(highest):
    areas = copy.deepcopy(tmp)
    for x in range(N):
        for y in range(N):
            if areas[x][y] > w:
                areas[x][y] = -1
    cnt = 0
    for x in range(N):
        for y in range(N):
            if areas[x][y] == -1:
                cnt += 1
                queue.append([x, y])
                areas[x][y] = 0
                while queue:
                    safe = queue.popleft()
                    for i in range(4):
                        xx = safe[0] + dx[i]
                        yy = safe[1] + dy[i]
                        if 0 <= xx < N and 0 <= yy < N and areas[xx][yy] == -1:
                            queue.append([xx, yy])
                            areas[xx][yy] = 0
    answer = max(answer, cnt)

print(answer)