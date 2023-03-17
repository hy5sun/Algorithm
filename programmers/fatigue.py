from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for dg in permutations(dungeons, len(dungeons)):
        now = k
        count = 0
        for cases in dg:
            if cases[0] <= now:
                now -= cases[1]
                count += 1
        if count > answer:
            answer = count

    return answer