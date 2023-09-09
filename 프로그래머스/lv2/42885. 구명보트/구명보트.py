def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    left, right = 0, len(people)-1
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1
        answer += 1
        left += 1
    return answer