from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

def DFS(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == 0:
            DFS(graph, i, visited)

if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = [[] for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (N + 1)
    DFS(graph, V, visited)
    print()
    visited = [0] * (N + 1)
    BFS(graph, V, visited)
