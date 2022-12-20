def fact(num):
    answer = 1
    for i in range(1, num+1):
        answer *= i;
    return answer

n, k = map(int, input().split())

ans = fact(n) / (fact(n-k) * fact(k))
print(int(ans))