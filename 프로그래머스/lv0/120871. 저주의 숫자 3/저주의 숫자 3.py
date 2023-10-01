def solution(n):
    notThree = [i for i in range(1, 2 * n + 1) if i % 3 != 0 and '3' not in str(i)]
    print(notThree)
    return notThree[n-1]
