n = int(input())
tallerthan = list(map(int, input().split()))
people = [0] * n

for t in range(len(tallerthan)):
    cnt = 0
    for i in range(len(people)):
        if cnt == tallerthan[t] and people[i] == 0:
            people[i] = str(t+1)
            break
        elif people[i] == 0:
            cnt += 1

print(' '.join(people))