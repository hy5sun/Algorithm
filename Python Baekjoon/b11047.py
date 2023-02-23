# 그리디 알고리즘
n, money = map(int, input().split())
coin = []
ans = 0
for _ in range(n):
    coin.append(int(input()))

coin.reverse()

for c in coin:
    i = money // c
    money -= i * c
    ans += i
print(ans)