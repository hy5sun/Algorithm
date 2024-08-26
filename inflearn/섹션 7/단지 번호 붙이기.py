from collections import deque

N = int(input())
house_map = []
for _ in range(N):
    house = list(map(int, input()))
    house_map.append(house)
apartment_complex = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque([])

for i in range(N):
    for j in range(N):
        if house_map[i][j] == 1:
            queue.append([i, j])
            house_map[i][j] = 0
            cnt = 1
            while queue:
                h = queue.popleft()
                for k in range(4):
                    x = h[0] + dx[k]
                    y = h[1] + dy[k]
                    if 0 <= x < N and 0 <= y < N:
                        if house_map[x][y] == 1:
                            cnt += 1
                            house_map[x][y] = 0
                            queue.append([x, y])
            apartment_complex.append(cnt)

apartment_complex.sort()
print(len(apartment_complex))
for cplx in apartment_complex:
    print(cplx)