X = int(input())
lst = [0] * (X+1)

for xx in range(2, X + 1):
    lst[xx] = lst[xx - 1] + 1
    if xx % 2 == 0:
        lst[xx] = min(lst[xx], lst[xx // 2] + 1)
    if xx % 3 == 0:
        lst[xx] = min(lst[xx], lst[xx // 3] + 1)

print(lst[X])