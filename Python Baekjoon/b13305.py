# 그리디 알고리즘
n = int(input())
distance = list(map(int, input().split()))
city = list(map(int, input().split()))
money = 0
lastDistance = sum(distance)
minPrice = city[0]
minIndex = city.index(min(city[:-1]))

for i in range(minIndex):
    if minPrice > city[i]:
        minPrice = city[i]
    money += minPrice * distance[i]
    lastDistance -= distance[i]

money += city[minIndex] * lastDistance
print(money)