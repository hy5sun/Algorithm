import itertools
numbers="011"
answer = 0
num = []

for i in range(1, len(numbers) +1):
    num += set(itertools.permutations(list(numbers), i))

print(num)

for n in num:
    if n[0] == '0':
        del n
        continue
    number = int(''.join(n))
    prime = True
    if number == 1:
        prime = False
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        answer += 1

print(answer)