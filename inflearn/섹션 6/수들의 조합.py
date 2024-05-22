def DFS(L, idx):
    global cnt
    if L == k:
        if sum(answer) % m == 0:
            cnt += 1
        return
    else:
        for i in range(idx, n):
            if nums[i] not in answer:
                answer[L] = nums[i]
                DFS(L+1, i+1)
                answer[L] = 0
        return cnt

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    answer = [0] * k
    print(DFS(0, 0))