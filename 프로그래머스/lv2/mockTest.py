from itertools import chain, repeat

def solution(answers):
    answer = []
    count = [0, 0, 0]
    a = list(chain.from_iterable(repeat([1, 2, 3, 4, 5], len(answers) // 5 + 1)))
    b = list(chain.from_iterable(repeat([2, 1, 2, 3, 2, 4, 2, 5], len(answers)//8 + 1)))
    c = list(chain.from_iterable(repeat([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], len(answers)//10 + 1)))

    for i in range(len(answers)):
        if a[i] == answers[i]:
            count[0] += 1
        if b[i] == answers[i]:
            count[1] += 1
        if c[i] == answers[i]:
            count[2] += 1

    for c in range(len(count)):
        if count[c] == max(count):
            answer.append(c + 1)

    return answer