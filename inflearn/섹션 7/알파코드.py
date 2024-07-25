import sys

def DFS(L, string):
    global cnt
    if L == length:
        print(string, end='\n')
        cnt += 1
        return
    else:
        for i in range(1, 3):
            if code[L] == '0':
                return
            else:
                if i == 1:
                    DFS(L+1, string+chr(64+int(code[L])))
                else:
                    nums = ''
                    if L+2 <= length:
                        for c in code[L:L+2]:
                            nums += c
                        nums = int(nums)
                        if nums <= 26:
                            DFS(L+i, string+chr(64+int(nums)))
                        else:
                            return

if __name__ == "__main__":
    code = list(input())
    if code == '0':
        sys.exit()
    length = len(code)
    string = ''
    cnt = 0
    DFS(0, '')
    print(cnt)