n, m = map(int, input().split(" "))
answer = 0
ansList = []

for _ in range(n):
    ansList.append(input())

for _ in range(m):
    inputStr = input()
    if inputStr in ansList:
        answer += 1

print(answer)