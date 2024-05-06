from collections import deque

n, k = map(int, input().split())

queue = deque(i for i in range(1, n+1))
answer = '<'

while len(queue) != 0:
    for _ in range(k-1):
        queue.append(queue.popleft())
    answer += str(queue.popleft()) + ', '

answer = answer[:-2]
answer += '>'
print(answer)
