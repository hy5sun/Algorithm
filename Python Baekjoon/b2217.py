# 그리디 알고리즘
n = int(input())
num = []
ans = []
for _ in range(n):
    num.append(int(input()))

num.sort(reverse=True)
for i in range(1, n+1):
    ans.append(num[i-1] * i)

print(max(ans))