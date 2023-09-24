n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

for i in range(1, len(nums)):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        elif j == len(nums[i]) - 1:
            nums[i][j] += nums[i - 1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j], nums[i-1][j-1])

print(max(nums[n-1]))
