def two(n):
    if n // 2 == 1:
        answer.append(n%2)
        answer.append(n//2)
        print(''.join(str(a) for a in answer[::-1]))
    else:
        answer.append(n % 2)
        n //= 2
        two(n)

n = int(input())
answer = []
two(n)
