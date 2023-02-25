# 그리디 알고리즘 (해결X/시간초과)
num = list(map(int,input()))
ans = 0

for i in range(len(num)):
    ans += num[i] * 10 ** i

if ans % 30 == 0:
    print(ans)
else:
    print(-1)
