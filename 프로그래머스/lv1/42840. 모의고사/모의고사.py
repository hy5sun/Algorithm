def solution(answers):
    answer = []
    correct = [0 for _ in range(3)]
    
    n1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    n2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)
    
    for i in range(len(answers)):
        if answers[i] == n1[i]:
            correct[0] += 1
        if answers[i] == n2[i]:
            correct[1] += 1
        if answers[i] == n3[i]:
            correct[2] += 1
    
    for i in range(len(correct)):
        if max(correct) == correct[i]:
            answer.append(i+1)
    return answer