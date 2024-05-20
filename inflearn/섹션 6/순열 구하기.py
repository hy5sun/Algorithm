def DFS(i):
    global cnt
    global answer
    if i > m:
        return
    if i == m:
        for a in answer:
            print(a, end=' ')
        print()
        cnt += 1
    else:
        for nn in range(1, n+1):
            if nn not in answer:
                answer[i] = nn
                DFS(i+1)
                answer[i] = 0
        return cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    answer = [0] * m
    print(DFS(0))