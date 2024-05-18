def DFS(cnt, total):
    global answer
    if cnt > answer:
        return
    if total > m:
        return
    if total == m:
        if cnt < answer:
            answer = cnt
        return
    else:
        for j in range(n):
            DFS(cnt+1, total + coins[j])

if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    coins.sort(reverse=True)

    answer=999999999999999
    DFS(0, 0)
    print(answer)
