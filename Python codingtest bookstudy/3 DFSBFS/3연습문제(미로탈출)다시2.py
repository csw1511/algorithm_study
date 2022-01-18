from collections import deque

n, m = map(int, input().split())

visited = []

for i in range(n):
    tmp = list(map(int,input()))

    visited.append(tmp)

def bfs(visited, v1, v2):
    que = deque()
    que.append((v1,v2))
    visited[v1][v2] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while que:
        v = que.popleft()
        
        for i in range(4):
            nextx = v[0]+dx[i]
            nexty = v[1]+dy[i]

            if nextx < n and nextx >=0 and nexty < m and nexty >=0:
                if visited[nextx][nexty] == 1:
                    que.append((nextx,nexty))
                    visited[nextx][nexty] += visited[v[0]][v[1]]
        
bfs(visited,0,0)


print(visited[n-1][m-1])



"""
입력예시

5 6
101010
111111
000001
111111
111111

예상 출력값 : 10

"""