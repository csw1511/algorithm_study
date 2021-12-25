from collections import deque

a, b = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for i in range(b):
    graph.append(list(map(int, input().split())))

pos1_x = []
pos1_y = []
for i in range(b):
    for j in range(a):
        if graph[i][j] == 1:
            pos1_x.append(i)
            pos1_y.append(j)


def bfs(x, y):
    que = deque()
    for i in range(len(x)):
        que.append((x[i], y[i]))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=b or ny<0 or ny>=a:
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))
    result = 0
    for i in range(b):
        for j in range(a):
            result = max(result, graph[i][j])
            if graph[i][j] == 0:
                return -1
    
    return result-1


print(bfs(pos1_x, pos1_y))
