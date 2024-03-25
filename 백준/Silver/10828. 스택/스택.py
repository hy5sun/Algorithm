import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline()

    if command == 'top\n':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command == 'size\n':
        print(len(stack))
    elif command == 'empty\n':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'pop\n':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        command = command.split()
        stack.append(int(command[1]))
