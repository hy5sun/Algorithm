word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in croatia:
    word = word.replace(char, "1")

print(len(word))