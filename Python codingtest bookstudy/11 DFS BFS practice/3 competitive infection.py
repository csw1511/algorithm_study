from collections import deque

n, k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

s, x, y = map(int, input().split())

viruslist = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            viruslist.append((graph[i][j], i, j))


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(graph, viruslist):
    q = deque()

    viruslist.sort()
    for i in viruslist:
        q.append(i)
    
    count = 0
    while q:
        if s == count:
            return graph[x-1][y-1]
        vlist = []
        lenq = len(q)

        for i in range(lenq):
            vlist.append(q.popleft())
        
        for i in vlist:
            for j in range(4):
                nextv1 = i[1] + dx[j]
                nextv2 = i[2] + dy[j]
                if nextv1 >= 0 and nextv1 < n and nextv2 >= 0 and nextv2 < n:
                    if graph[nextv1][nextv2] == 0:
                        q.append((i[0], nextv1, nextv2))
                        graph[nextv1][nextv2] = i[0]
        
        count += 1
    return graph[x-1][y-1]


print(bfs(graph,viruslist))
"""
3 3
1 0 2
0 0 0
3 0 0
3 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2


7 12031
3 0 0 5 0 2 0
0 0 0 2 0 5 1
0 2 3 0 0 0 0
0 0 0 0 1 0 3
0 0 5 0 0 0 0
2 0 0 4 0 0 0
4 0 3 0 0 5 0
3 6 5
"""



    
