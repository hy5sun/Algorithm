import random

heights = []
for _ in range(9):
    heights.append(int(input()))

while(sum(heights) != 100):
    fake = random.sample(heights, 2)
    if (sum(fake) == sum(heights) - 100):
        for j in fake:
            heights.remove(j)

heights.sort()
for i in heights:
    print(i)