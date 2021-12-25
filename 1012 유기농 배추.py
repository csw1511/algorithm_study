from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    quee = deque()
    quee.append((x,y))
    while quee:
        x, y = quee.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                quee.append((nx, ny))
                        
        

for _ in range(t):
    m, n, k = map(int, input().split())
    
    graph = [[0]*m for _ in range(n)]
        
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1


    count = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(a, b, graph)
                count += 1
    
    print(count)
