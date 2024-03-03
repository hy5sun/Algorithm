def Anagram(wordA, wordB):
    words = {}

    for wa in wordA:
        words[wa] = words.get(wa, 0) + 1

    for wb in wordB:
        words[wb] = words.get(wb, 0) - 1

    for w, cnt in words.items():
        if cnt != 0:
            return "NO"
            break

    return "YES"

wordA = input()
wordB = input()
print(Anagram(wordA, wordB))