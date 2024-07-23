def Maximum_Profit(L, total):
    global max_profit
    if L == N:
        if total > max_profit:
            max_profit = total
        return
    else:
        if L+work[L][0] <= N:
            Maximum_Profit(L+work[L][0], total+work[L][1])
        Maximum_Profit(L+1, total)

if __name__ == "__main__":
    N = int(input())
    max_profit = 0
    answer = 0
    work = []
    for _ in range(N):
        T, P = map(int, input().split())
        work.append([T, P])
    Maximum_Profit(0, 0)
    print(max_profit)
