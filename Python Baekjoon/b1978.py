size = int(input())
num = list(map(int, input().split()))
count = 0
sosu = []

for j in range(2, 32):
    if (j == 2 or j == 3 or j == 5):
        sosu.append(j)
    elif (j % 2 != 0 and j % 3 != 0 and j % 5 != 0):
        sosu.append(j)

for i in num:
    for j in sosu:
        if (i == j):
            count += 1
            break
        elif (i == 1 or i % j == 0):
            break
        elif (i % j != 0 and j == sosu[len(sosu) - 1]):
            count += 1

print(count)