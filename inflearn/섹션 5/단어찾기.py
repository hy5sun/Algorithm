n = int(input())
word = {}

for _ in range(n):
    word[input()] = 1

for _ in range(n-1):
    word[input()] = 0

for w, cnt in word.items():
    if cnt == 1:
        print(w)