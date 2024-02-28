n, m = map(int, input().split())
people = list(map(int, input().split()))

people.sort(reverse=True)
cnt = 0

while len(people) != 0:
    if len(people) == 1:
        cnt += 1
        break
    if people[0] + people[-1] <= m:
        cnt += 1
        people.pop()
        del people[0]
    else:
        cnt += 1
        del people[0]

print(cnt)