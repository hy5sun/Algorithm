from collections import deque

n, k = map(int, input().split())
queue = deque(i for i in range(1, n+1))

for i in range(n-1):
    for j in range(k-1):
        pass_person = queue.popleft()
        queue.append(pass_person)
    queue.popleft()

print(queue[0])