selfNums = [i for i in range(1, 10000)]

for i in range(1, 10000):
    not_selfNum = i + sum(int(x) for x in str(i))
    if not_selfNum in selfNums:
        selfNums.remove(not_selfNum)

for i in selfNums:
    print(i)

