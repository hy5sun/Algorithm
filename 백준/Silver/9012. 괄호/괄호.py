import sys

input = sys.stdin.readline

def IsVPS(data):
    stack = []
    for d in data:
        if d == '(':
            stack.append('(')
        elif d == ')':
            if stack:
                stack.pop()
            else:
                return 'NO'

    if stack:
        return "NO"
    else:
        return "YES"

n = int(input())

for i in range(n):
    data = input()
    print(IsVPS(data))
