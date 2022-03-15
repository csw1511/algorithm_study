from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0] * (n+1)

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        node = q.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i]=visited[node] + 1
                q.append(i)

bfs(graph,x,visited)

isCity = False
for i in range(len(visited)):
    if visited[i] == k:
        print(i)
        isCity = True

if not isCity:
    print('-1')


"""
4 4 2 1
1 2
1 3
2 3
2 4
"""