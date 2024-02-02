n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lt = 0
rt = n-1
mid = (lt + rt) // 2

while nums[mid] != m:
    if nums[mid] > m:
        mid -= 1
    elif nums[mid] < m:
        mid += 1
    else:
        break

print(mid+1)