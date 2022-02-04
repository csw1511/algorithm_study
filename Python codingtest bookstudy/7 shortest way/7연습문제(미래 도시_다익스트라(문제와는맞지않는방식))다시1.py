import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] *(n+1)

for _ in range(m):
    a, b= map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x, k = map(int,input().split())


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
go1k = distance[k]

distance = [INF] *(n+1)
dijkstra(k)
gokx = distance[x]

go1kx = go1k + gokx

if go1kx > INF:
    print(-1)
else:
    print(go1kx)

"""
입력값
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
출력값
3

입력값
4 2
1 3
2 4
3 4
출력값
-1
"""