from collections import deque


n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(n+1):
    graph[i].sort()


## graph done.

visD = [False] * (n+1) ##visited arr for dfs
visB = [False] * (n+1) ##visited arr for bfs

def dfs(graph, v, visited):
    if visited[v] == True:
        return;
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        dfs(graph, i, visited)

def bfs(graph, start, visited):
    quee = deque()
    quee.append(start)

    while quee:
        v = quee.popleft()
        visited[v] = True
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                quee.append(i)
                visited[i] = True

        

dfs(graph, v, visD)
print()
bfs(graph, v, visB)
