def to_minus_binary(n):
    if n == 0:
        return
    else:
        to_minus_binary(n//2 * (-1))
        print(n % 2, end= '')

n = int(input())

if n == 0:
    print(0)
else:
    to_minus_binary(n)