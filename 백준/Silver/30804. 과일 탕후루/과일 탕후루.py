import sys

N = int(input())
lst = list(map(int, input().split()))

if N == 1:
    print(N)
    sys.exit()

answer = 0
L = 0
R = 1
fruit = set([lst[L], lst[R]])
cnt = [0] * 9
cnt[lst[L]-1] += 1
cnt[lst[R]-1] += 1
tanghulu = 2

while L != N:
    if R < N and len(fruit) <= 2:
        R += 1
        tanghulu += 1
        if R != N:
            fruit.add(lst[R])
            cnt[lst[R]-1] += 1
    else:
        tanghulu -= 1
        answer = max(answer, tanghulu)
        cnt[lst[L]-1] -= 1
        if cnt[lst[L]-1] == 0:
            fruit.remove(lst[L])
        L += 1

print(answer)
