def Anagram(wordA, wordB):
    words = {}

    for wa in wordA:
        words[wa] = words.get(wa, 0) + 1

    for wb in wordB:
        words[wb] = words.get(wb, 0) - 1

    for w, cnt in words.items():
        if cnt != 0:
            return "{} & {} are NOT anagrams.".format(wordA, wordB)
            break

    return "{} & {} are anagrams.".format(wordA, wordB)

n = int(input())
word = []

for _ in range(n):
    word.append(input().split())

for ww in word:
    print(Anagram(ww[0], ww[1]))