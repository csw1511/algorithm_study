import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(1)
result1 = distance[k]
distance = [INF]* (n+1)

dijkstra(k)
result2= distance[x]
result = result1 + result2
if result > 2*m:
    print(-1)
else:
    print(result1 + result2)
