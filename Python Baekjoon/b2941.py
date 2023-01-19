word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(croatia)):
    if croatia[i] in word:
        word = word.replace(croatia[i], "1")

print(len(word))