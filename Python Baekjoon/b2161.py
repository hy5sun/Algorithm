nums = int(input())
a = []
ans = []

for i in range(1, nums+1):
    a.append(i)

while (len(a) != 0):
    ans.append(a.pop(0))
    if(len(a) > 1):
        a.append(a.pop(0))

for j in ans:
    print(j, end =" ")