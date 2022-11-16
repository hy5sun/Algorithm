size = int(input())
strr = []
for i in range(size):
    strr.append(input())

for _ in range(size):
    for i in range(size-1):
        if len(strr[i]) > len(strr[i+1]):
            a = strr[i]
            strr[i] = strr[i+1]
            strr[i+1] = a

    for j in range(size-1):
        if len(strr[j]) == len(strr[j+1]):
            if (strr[j] > strr[j+1]):
                b = strr[j]
                strr[j] = strr[j+1]
                strr[j+1] = b
print(strr)