import sys

def DFS(v, cnt):
    if cnt == 5:
        print(1)
        sys.exit()
    else:
        for i in lst[v]:
            if ch[i] == 0:
                ch[i] = 1
                DFS(i, cnt+1)
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = [[] for _ in range(n)]
    ch = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    for k in range(n):
        ch[k] = 1
        DFS(k, 1)
        ch[k] = 0
    print(0)
