import abc
from collections import deque
from unittest import TextTestResult

def bfs(graph, v1, v2):
    q = deque()
    q.append((v1,v2))
    graph[v1][v2] = 2

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        n1, n2 = q.popleft()

        for i in range(4):
            nextv1 = n1 + dx[i]
            nextv2 = n2 + dy[i]
            if nextv1 >= 0 and nextv1 < n and nextv2 >=0 and nextv2 < m:
                if graph[nextv1][nextv2] == 0:
                    q.append((nextv1,nextv2))
                    graph[nextv1][nextv2] = 2

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

startarr = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            startarr.append((i,j))




"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""