def Expression_Count(remain):
    global cnt
    if remain < 0:
        return
    if remain == 0:
        cnt += 1
        return
    else:
        for i in range(1, 4):
            Expression_Count(remain-i)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        cnt = 0
        Expression_Count(int(input()))
        print(cnt)