def to_binary(n):
    if n == 0:
        return
    else:
        to_binary(n // 2)
        print(n % 2, end='')

n = int(input())
to_binary(n)