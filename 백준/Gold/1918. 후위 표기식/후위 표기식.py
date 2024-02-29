before = input()
stack = []
answer = ''

for b in before:
    if b not in '+-*/()':
        answer += b
    else:
        if b == '(':
            stack.append(b)
        elif b == '*' or b == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(b)
        elif b == '+' or b == '-':
            while stack and (stack[-1] != '('):
                answer += stack.pop()
            stack.append(b)
        elif b == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)
