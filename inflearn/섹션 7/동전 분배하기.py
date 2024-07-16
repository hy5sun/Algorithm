def DFS(L):
    global answer
    if L == N:
        difference = max(people) - min(people)
        if difference < answer and len(set(people)) == 3:
            answer = difference
        return
    else:
        for i in range(3):
            people[i] += coins[L]
            DFS(L+1)
            people[i] -= coins[L]

if __name__ == "__main__":
    N = int(input())
    coins = []
    people = [0] * 3
    answer = 9999999
    for _ in range(N):
        coins.append(int(input()))
    DFS(0)
    print(answer)
