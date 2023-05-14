def solution(elements):
    answer = set()
    double = elements + elements
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum(double[i:i+j+1]))
    return len(answer)