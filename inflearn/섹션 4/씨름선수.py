n = int(input())
player = []
for _ in range(n):
    h, w = map(int, input().split())
    player.append((h, w))

cnt = 0
player.sort()

for i in range(len(player)):
    for j in range(i+1, len(player)):
        if player[i][1] < player[j][1]:
            cnt += 1
            break

print(n-cnt)
