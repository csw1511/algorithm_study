from dis import dis
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

distance = [INF]*(n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0   #이 부분 놓침. 시작노드는 방문했고, 이를 0으로 표시해야 후속노드들 거리가 잘 계산됨
                        #또한 0으로 해도 distance[now] < dist를 만족시키지 않기에 정상적으로 처리함.

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:   #
                distance[i[0]] = cost   #둘 모두 distance[i]로 쓰는 실수를 함. i는 그래프[now]의 요소이므로
                                        #i의 type은 튜플이다.
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
largest = max(distance[1:])
for i in distance:
    if i < INF and i != 0:
        count += 1

print(count, largest)

"""
입력값
6 11 1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
출력값
5 4

입력값
3 2 1
1 2 4
1 3 2
출력값
2 4
"""