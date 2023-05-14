def solution(elements):
    answer = set()
    double = elements + elements
    for i in range(len(elements)):
        j = 0
        for _ in range(len(elements)):
            answer.add(sum(double[i:i+j+1]))
            j += 1
    return len(answer)