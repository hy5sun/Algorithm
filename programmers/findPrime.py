import itertools, math

def isprime(n):  # 에라토스테네스의 체
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num = set()
    for i in range(1, len(numbers) + 1):
        num |= set(map(int, map(''.join, itertools.permutations(list(numbers), i))))

    num -= set(range(2))

    for n in num:
        if isprime(n):
            answer += 1
    return answer