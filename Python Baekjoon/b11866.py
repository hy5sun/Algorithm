# deque 사용
from collections import deque

n, k = map(int, input().split())
nums = deque(i for i in range(1, n+1))
answer = []

while nums:
    for i in range(k-1):
        nums.append(nums.popleft())
    answer.append(nums.popleft())


# 1 2 4 5 6 7
print("<" + ', '.join(map(str, answer)) + ">")