def solution(s):
    nums = list(map(int, s.split(' ')))
    return f'{min(nums)}' + ' ' + f'{max(nums)}'