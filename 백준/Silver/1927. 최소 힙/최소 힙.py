import heapq
import sys

size = int(sys.stdin.readline())
nums = []
myHeap = []

for _ in range(size):
    nums = int(sys.stdin.readline())

    if (nums > 0):
        heapq.heappush(myHeap, nums)
    elif (len(myHeap) == 0):
        print(heapq.heappushpop(myHeap, 0))
    else:
        print(heapq.heappop(myHeap))