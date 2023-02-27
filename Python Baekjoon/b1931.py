# 그리디 알고리즘 (시간초과..)
n = int(input())
time = []
meetingTime = []
count = 0

for i in range(n):
    start, end = map(int, input().split())
    spending = end - start
    time.append([start, end, spending])

    time.sort()
    time.sort(key=lambda time: time[2])

    for x in range(start, end):
        if x in meetingTime:
            spending -= 1

    if spending == end - start:
        count += 1
        for x in range(start, end):
            meetingTime.append(x)

print(count)