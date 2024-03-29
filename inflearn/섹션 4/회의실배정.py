n = int(input())
time = []

for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time.sort(key=lambda x: (x[1], x[0]))
end = time[0][1]
cnt = 1

for i in range(1, len(time)):
    if time[i][0] >= end:
        cnt += 1
        end = time[i][1]

print(cnt)
