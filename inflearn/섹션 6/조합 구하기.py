def DFS(L):
    global cnt
    if L == m:
        for a in answer:
            print(a, end=' ')
        print()
        cnt += 1
    else:
        start = answer[L-1] + 1
        for num in range(start, n+1):
            if num not in answer:
                answer[L] = num
                DFS(L+1)
                answer[L] = 0
        return cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    answer = [0] * m
    print(DFS(0))
