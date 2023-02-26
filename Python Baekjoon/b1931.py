# 그리디 알고리즘 (해결X)
n = int(input())
time = []
meetingTime = []
count = 0

for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end, end - start])

time.sort()
time.sort(key=lambda time: time[2])

for i in range(n):
    a = [x for x in range(time[i][0], time[i][1])]
    for j in a:
        if j in meetingTime:
            break
    meetingTime.append(q for q in a)
    count += 1

print(count)

# [3, 5], [5, 7], [12, 14], [1, 4], [8, 11]
