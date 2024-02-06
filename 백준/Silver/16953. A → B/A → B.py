def b16953(data):
    A, B = map(int, data)
    cnt = 1

    while True:
        if B % 2 == 0:
            B //= 2
            cnt += 1
        elif B % 10 == 1:
            B = list(str(B))
            B.pop()
            cnt += 1

            if len(B) != 1:
                B = int(''.join(B))
            else:
                B = int(B[0])
        else:
            return -1

        if A == B:
            return cnt
        elif A > B:
            return -1

print(b16953(input().split()))
