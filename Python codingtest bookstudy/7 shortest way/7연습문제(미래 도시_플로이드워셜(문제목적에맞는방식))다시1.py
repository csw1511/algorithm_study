import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

go1k = graph[1][k]
gokx = graph[k][x]

if go1k + gokx < INF:
    print(go1k + gokx)
else:
    print(-1)


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