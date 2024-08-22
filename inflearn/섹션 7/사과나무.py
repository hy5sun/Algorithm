from collections import deque

N = int(input())
trees = []
for _ in range(N):
    apples = list(map(int, input().split()))
    trees.append(apples)
answer = 0
queue = deque([[N//2, N//2]])
visited = [[0] * N for i in range(N)]
cnt = 0
for i in range(1, N, 2):
    cnt += i * 2
cnt += N

while queue:
    next = queue.popleft()
    if cnt == 0:
        break
    if 0 <= next[0] < N and 0 <= next[1] < N:
        if visited[next[0]][next[1]] == 0:
            answer += trees[next[0]][next[1]]
            cnt -= 1
            visited[next[0]][next[1]] = 1
            queue.append([next[0]+1, next[1]])
            queue.append([next[0], next[1]+1])
            queue.append([next[0]-1, next[1]])
            queue.append([next[0], next[1]-1])

print(answer)

