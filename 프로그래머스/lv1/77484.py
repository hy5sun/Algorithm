def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    same = 0
    for l in lottos:
        if l in win_nums:
            same += 1
    return [rank[same+lottos.count(0)], rank[same]]