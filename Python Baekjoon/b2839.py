# 그리디 알고리즘
sugar = int(input())
ans = []

for i in range(5000//5+1):
    for j in range(5000//3+1):
        if i * 5 + j * 3 == sugar:
            ans.append(i+j)
            break

if len(ans) == 0:
    ans.append(-1)

print(min(ans))