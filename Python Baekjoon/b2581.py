startNum = int(input())
endNum = int(input())
sosu = []

for i in range(startNum, endNum + 1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if ( i % j == 0):
                error += 1
        if (error == 0):
            sosu.append(i)

if len(sosu) != 0:
    print(sum(sosu))

    print(min(sosu))

else:
    print(-1)
