def DFS(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n+1):
            if nums[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * (n+1)
    nums = [[0] * (n+1) for _ in range(n+1)]
    cnt = 0

    for i in range(m):
        num1, num2 = map(int, input().split())
        nums[num1][num2] = 1

    ch[1]=1
    DFS(1)
    print(cnt)