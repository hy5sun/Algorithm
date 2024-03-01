essential = list(input())
n = int(input())
plan = []

for i in range(n):
    plan.append(input())

for i in range(n):
    ess = []

    for p in plan[i]:
        if (p in essential) and (p not in ess):
            ess.append(p)

    if ess == essential:
        print("#{} YES".format(i+1))
    else:
        print('#{} NO'.format(i+1))