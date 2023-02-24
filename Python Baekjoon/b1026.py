# 그리디 알고리즘
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

for _ in range(n):
    ans += min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))

print(ans)