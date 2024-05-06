string = list(input())

non = False
stack = []

for s in string:
    if s == ' ' or s == '<':
        print(''.join(stack[::-1]), end='')
        stack = []
        if s == '<':
            non = True
        else:
            print(' ', end='')
            continue

    if non:
        print(s, end='')
    else:
        stack.append(s)

    if s == '>':
        non = False

if stack:
    print(''.join(stack[::-1]), end='')