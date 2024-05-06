import sys

def DFS(L, sum_num): # 원소 인덱스, 총합
    if sum_num > total // 2: # total의 절반 값을 넘어가면 같을 일이 없음
        return
    if L == n:
        if sum_num == total - sum_num:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum_num + nums[L]) # 해당 원소 포함
        DFS(L+1, sum_num) # 해당 원소 미포함

if __name__ == "__main__":
    n = int(input())
    nums = map(int, input().split())
    total = sum(nums)
    DFS(0, 0)
    print("NO")
