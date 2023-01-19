n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]
index = k - 1

print("<", end = "")

for i in range(n):
    print(nums[index], end='')
    nums.remove(nums[index])

    index += k - 1

    while not index < len(nums):
        index -= len(nums)
        if len(nums) == 0:
            break

    if not len(nums) == 0:
        print(', ', end="")

print(">")