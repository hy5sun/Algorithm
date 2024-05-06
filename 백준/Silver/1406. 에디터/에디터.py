import sys

input = sys.stdin.readline

stack = list(input().strip())
tmp = []
m = int(input())

for _ in range(m):
    command = input().split()

    if command[0] == 'L':
        if stack:
            tmp.append(stack.pop())
    elif command[0] == 'D':
        if tmp:
            stack.append(tmp.pop())
    elif command[0] == 'B':
        if stack:
            stack.pop()
    elif command[0] == 'P':
        stack.append(command[1])

for i in range(len(tmp)-1, -1, -1):
    stack.append(tmp[i])

print(''.join(stack))
