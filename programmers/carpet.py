import math

def solution(brown, yellow):
    area = brown + yellow

    for h in range(3, int(math.sqrt(area) + 1)):
        w = area // h
        if brown == w * h - yellow and yellow == (w - 2) * (h - 2):
            return [w, h]