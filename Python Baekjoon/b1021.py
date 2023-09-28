n, m = map(int, input().split())
nums = list(map(int, input().split()))
queue = [i for i in range(1, n+1)]
count = 0

while len(nums) != 0:
    if queue[0] == nums[0]:
        del nums[0]
        del queue[0]
        continue

    if len(queue) // 2 >= queue.index(nums[0]):
        queue.append(queue[0])
        del queue[0]
        count += 1

    else:
        n = queue.pop()
        queue.insert(0, n)
        count += 1

print(count)
