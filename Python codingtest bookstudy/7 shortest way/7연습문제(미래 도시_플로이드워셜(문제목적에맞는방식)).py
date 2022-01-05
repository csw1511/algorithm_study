import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for i in range(n+1)]

for a in range(1, n+1): #자기자신과의 거리는 0임을 반드시 초기화시켜주어야 한다
    for b in range(1, n+1):
        if a== b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for t in range(1, n+1): #보니까 여기 iter가 k여도 별 상관없이 잘 동작하나보다
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])

result1 = graph[1][k]

result2 = graph[k][x]

result = result1 + result2

if result >= INF:
    print(-1)
else:
    print(result)
    
