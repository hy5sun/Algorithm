n = int(input())
nums = list(map(int, input().split()))
answer = []

for i in range(n, 0, -1):
    answer.insert(nums[i-1], i)

for a in answer:
    print(a, end=' ')
