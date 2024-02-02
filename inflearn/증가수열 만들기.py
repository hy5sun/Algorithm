n = int(input())
nums = list(map(int, input().split()))
lst = [0]
answer = ''

lt = 0
rt = n-1

while lt <= rt:
    if nums[lt] < lst[-1] and nums[rt] < lst[-1]:
        break

    if nums[lt] < nums[rt]:
        if nums[lt] > lst[-1]:
            lst.append(nums[lt])
            lt += 1
            answer += 'L'
        else:
            lst.append(nums[rt])
            rt -= 1
            answer += 'R'
    else:
        if nums[rt] > lst[-1]:
            lst.append(nums[rt])
            rt -= 1
            answer += 'R'
        else:
            lst.append(nums[lt])
            lt += 1
            answer += 'L'

print(len(lst)-1)
print(answer)