def Anagram(wordA, wordB):
    words = {}

    for wa in wordA:
        if wa not in words:
            words[wa] = 1
        else:
            words[wa] += 1

    for wb in wordB:
        words[wb] -= 1

    for w, cnt in words.items():
        if cnt != 0:
            return "NO"
            break

    return "YES"

wordA = input()
wordB = input()
print(Anagram(wordA, wordB))