import sys
import heapq

size = int(sys.stdin.readline())
maxHeap = []
for _ in range(size):
    nums = int(sys.stdin.readline())

    if (nums != 0):
        heapq.heappush(maxHeap, (-1) * nums)
    else:
        try:
            print((-1) * heapq.heappop(maxHeap))
        except:
            print(0)