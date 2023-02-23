# 그리디 알고리즘
n = int(input())
time = list(map(int, input().split()))
ans = 0
time.sort()

for i in range(n):
    for j in range(i+1):
        ans += time[j]

print(ans)