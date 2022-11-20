size = int(input())
nums = []
for i in range(size):
    nums.append(int(input()))

nums.sort()

for j in nums:
    print(j)