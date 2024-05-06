
def DFS(v):
    # 전위순회 : 부모 -> 왼쪽 자식 -> 오른쪽 자식
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)

    # 중위순회 : 왼쪽 자식 -> 부모 -> 오르쪽 자식
    if v > 7:
        return
    else:
        DFS(v*2)
        print(v, end=' ')
        DFS(v*2+1)

    # 후위순회 : 왼쪽 자식 -> 오르쪽 자식 -> 부모
    if v > 7:
        return
    else:
        DFS(v*2)
        DFS(v*2+1)
        print(v, end=' ')

if __name__ == '__main__':
    DFS(1)