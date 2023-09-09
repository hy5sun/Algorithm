def solution(n):
    answer = 1 # 1로만 구성
    two = n // 2
    rest = n % 2
    for i in range(1, two+1):
        answer += combination(i, (two-i)*2 + rest)
    return answer % 1234567

def factorial(n):
    answer = 1
    if n == 0:
        return answer
    for i in range(1, n+1):
        answer *= i
    return answer

def combination(a, b):
    return factorial(a+b) // (factorial(a) * factorial(b))