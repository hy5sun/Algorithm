# 그리디 알고리즘
# < 제일 큰 수를 만든 후, 30의 배수인지 확인 >
num = list(input())
num.sort(reverse=True)

ans = int(''.join(num))

if ans % 30 == 0:
    print(ans)
else:
    print(-1)

''' < 30의 배수인지 확인 후, 가장 큰 수 출력 >
num = list(input())
num.sort(reverse=True)

if '0' in num:
    if sum(map(int, num)) % 3 == 0:
        print(int(''.join(num)))
    else:
        print(-1)

else:
    print(-1)
'''