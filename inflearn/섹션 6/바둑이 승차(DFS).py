def DFS(i, summ, interim_total):
    global max_sum
    if summ + (total - interim_total) < max_sum:
        return
    if summ > c:
        return
    if i == n:
        if max_sum < summ:
            max_sum = summ
    else:
        DFS(i+1, summ + nums[i], summ + nums[i])
        DFS(i+1, summ, summ + nums[i])
        return max_sum

if __name__ == "__main__":
    c, n = map(int, input().split())
    nums = []
    max_sum = 0

    for _ in range(n):
        nums.append(int(input()))

    total = sum(nums)
    print(DFS(0, 0, 0))
