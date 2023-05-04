def solution(s):
    s = s.lower()
    slist = list(s.split(' '))
    answer = []

    for s in slist:
        s = list(s)
        if len(s) != 0:
            s[0] = s[0].upper();
        answer.append(''.join(s))

    return ' '.join(answer)