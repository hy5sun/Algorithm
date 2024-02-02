k, n = map(int, input().split())
length = []
for _ in range(k):
    length.append(int(input()))

lt = 1
rt = max(length)

while lt <= rt:
    mid = (lt + rt) // 2
    line = 0

    for l in length:
        line += l // mid

    if line < n:
        rt = mid - 1
    else:
        lt = mid + 1

print(rt)