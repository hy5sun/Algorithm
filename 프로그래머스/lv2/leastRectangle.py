def solution(sizes):
    maxW = 0
    maxH = 0

    for w, h in sizes:
        if w < h:
            a = w
            w = h
            h = a
        maxW = max(maxW, w)
        maxH = max(maxH, h)
    return maxW * maxH