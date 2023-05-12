def solution(n):
    pb = [0, 1]
    for i in range(1, n):
        pb.append(pb[i] + pb[i-1])
    return pb[n] % 1234567
    