def solution(citations):
    answer = 0
    for h in range(1, len(citations)+1):
        count = 0
        for c in citations:
            if c >= h:
                count += 1
        if count == h:
            answer = max(answer, h)
    return answer

print(solution([6, 5, 5, 5, 3, 2, 1, 0]))