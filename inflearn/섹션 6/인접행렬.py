n, m = map(int, input().split())
answer = [[0] * n for _ in range(n)]

for _ in range(m):
    n1, n2, length = map(int, input().split())
    answer[n1-1][n2-1] = length

for a in answer:
    for aa in a:
        print(aa, end=' ')
    print()