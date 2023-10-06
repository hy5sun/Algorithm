def calculate(done, lines, answer, firstIdx, secodeIdx):
    cnt = 0
    if lines[firstIdx][0] >= lines[secodeIdx][0] and lines[firstIdx][0] < lines[secodeIdx][1]:
        if lines[firstIdx][1] >= lines[secodeIdx][1]:
            for j in range(lines[firstIdx][0], lines[secodeIdx][1]):
                if j in done:
                    continue
                else:
                    cnt += 1
                    done.append(j)
            answer += cnt
        else:
            for j in range(lines[firstIdx][0], lines[firstIdx][1]):
                if j in done:
                    continue
                else:
                    cnt += 1
                    done.append(j)
            answer += cnt
    return [done, answer]

def solution(lines):
    answer = 0
    lines.sort()
    done = []
    
    for i in range(1, len(lines)):
        done, answer = calculate(done, lines, answer, i, i-1)
        if i == 2:
            done, answer = calculate(done, lines, answer, i, i-2)

    return answer