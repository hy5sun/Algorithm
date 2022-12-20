a = int(input())
b = int(input())
c = int(input())
multi = list(str(a * b * c))

for i in range(10):
    count = 0
    for j in multi:
        if i == int(j):
            count += 1
    print(count)
