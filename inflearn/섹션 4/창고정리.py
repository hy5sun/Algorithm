l = int(input())
height = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    largest = max(height)
    smallest = min(height)
    height[height.index(largest)] -= 1
    height[height.index(smallest)] += 1

print(max(height)-min(height))