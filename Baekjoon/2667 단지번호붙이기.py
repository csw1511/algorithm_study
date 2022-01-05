from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    if graph[x][y] == 0:
        return 0
    quee = deque()
    quee.append((x,y))
    count = 0
    
    if graph[x][y] == 1:
        count +=1
        graph[x][y] = 0
    
    
    while quee:
        x, y = quee.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or ny <0 or nx >=n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                quee.append((nx, ny))
                graph[nx][ny] = 0
                ##print(nx, ny)
               
                count +=1
    return count


resultarr = []
county = 0

for i in range(n):
    for j in range(n):
        v = bfs(i, j)
        if v != 0:
            county += 1
            resultarr.append(v)
            
resultarr.sort()
print(county)
for i in resultarr:
    print(i)
            
