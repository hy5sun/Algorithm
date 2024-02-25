lines = list(input())
stack = []
answer = 0

for i in range(len(lines)):
    if lines[i] == '(':
        stack.append(lines[i])
    else:
        stack.pop()
        if lines[i-1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)
