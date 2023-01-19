n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]
index = k - 1
answer = []

for i in range(n):
    answer.append(nums[index])
    nums.remove(nums[index])

    index += k - 1

    while not index < len(nums):
        index -= len(nums)
        if len(nums) == 0:
            break

print("<" + ', '.join(map(str, answer)) + ">")