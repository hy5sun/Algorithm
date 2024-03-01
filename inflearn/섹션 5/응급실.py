from collections import deque

n, m = map(int, input().split())
danger = list(map(int, input().split()))
queue = deque()
cnt = 0

for i in range(n):
    queue.append((danger[i], i))

while True:
    tmp = queue.popleft()
    if tmp[0] < max(queue)[0]:
        queue.append(tmp)
    else:
        cnt += 1
        if tmp[1] == m:
            print(cnt)
            break
