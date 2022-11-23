import heapq
import sys

size = int(sys.stdin.readline())
myHeap = []

for i in range(size):
    nums = int(sys.stdin.readline())

    if (nums != 0):
        heapq.heappush(myHeap, nums)
    else:
        try:
            print(heapq.heappop(myHeap))
        except:
            print(0)
