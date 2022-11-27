n = int(input())
candidate = []
count = 0

for _ in range(n):
    candidate.append(int(input()))

while (1):
    if (candidate[0] == max(candidate) and candidate.count(max(candidate)) == 1):
        break

    i = candidate.index(max(candidate), 1, n)
    candidate[i] -= 1
    candidate[0] += 1
    count += 1

print(count)