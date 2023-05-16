import math
def solution(arr):
    for num in range(max(arr), math.prod(arr)+1):
        ps=True
        for a in arr:
            if num % a != 0:
                ps = False
                break
        if ps:
            return num