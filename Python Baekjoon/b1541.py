expression = input().split('-')

for i in range(len(expression)):
    if not '+' in expression[i]:
        expression[i] = int(expression[i])
    else:
        expression[i] = sum(map(int, expression[i].split('+')))

if len(expression) != 1:
    expression[0] = expression[0] - sum(expression[1:])

print(expression[0])