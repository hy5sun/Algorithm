def solution(string):
    answer = 0
    nums = [str(i) for i in range(10)]
    num = ''
    
    for i in range(len(string)):
        if string[i] in nums:
            num += string[i]
        else:
            if num:
                answer += int(num)
                num = ''
    if num:
        answer += int(num)
    return answer
            
