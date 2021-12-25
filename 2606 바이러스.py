from collections import deque

node = int(input())
edge = int(input())

graph=[[] for i in range(node+1)]


for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(node+1)

count = 0

def bfs(graph, start, visited, count):
    quee = deque()
    quee.append(start)
    visited[start] = True

    while quee:
        v = quee.popleft()
        for i in graph[v]:
            if visited[i] == False:
                quee.append(i)
                visited[i] = True
                count +=1
    return count
            
print(bfs(graph,1, visited, count))
    
