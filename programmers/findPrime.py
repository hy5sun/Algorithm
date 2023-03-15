import itertools, math
numbers = input()
answer = 0
num = set()

for i in range(1, len(numbers) +1):
    num |= set(map(int, map("".join, itertools.permutations(list(numbers), i))))

num -= set(range(2))

for n in num:
    prime = True
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            prime = False
            break
    if prime:
        answer += 1

print(answer)