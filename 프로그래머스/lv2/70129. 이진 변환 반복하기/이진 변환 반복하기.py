def solution(s):
    count = 0 # 이진 변환 횟수
    zero = 0 # 삭제된 0의 개수
    s = list(s)
    
    while len(s) != 1:
        zero += s.count('0')
        s = list(bin(s.count('1'))[2:])
        count += 1

    return [count, zero]