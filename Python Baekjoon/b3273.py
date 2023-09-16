n = int(input())
nums = [int(num) for num in input().split(" ")]
x = int(input())
cnt = 0
nums.sort()

left = 0
right = n-1

while left < right:
    if nums[left] + nums[right] > x:
        right -= 1
    else:
        if nums[left] + nums[right] == x:
            cnt += 1
        left += 1

print(cnt)