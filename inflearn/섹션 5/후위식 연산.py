formula = input()
stack = []
sign = ['+', '-', '*', '/']

for f in formula:
    if f not in sign: # isdecimal() 사용 가능
        stack.append(int(f))
    else:
        final = stack.pop()
        sec_final = stack.pop()
        if f == '+':
            stack.append(sec_final+final)
        elif f == '-':
            stack.append(sec_final-final)
        elif f == '*':
            stack.append(sec_final*final)
        elif f == '/':
            stack.append(sec_final//final)

print(stack[0])