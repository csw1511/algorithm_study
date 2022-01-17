N, M = map(int, input().split())

arr = [[0 for i in range(M)] for j in range(N)]

graph = [[] for _ in range(N * M)]

visited = [0] * (N * M)
##그래프와 방문여부 배열 생성

for i in range(N):  ##배열 입력
    temp = list(map(int, input().split()))
    arr[i] = temp
    for j in range(M):
        if arr[i][j] == 1:
            visited[i * M + j] = 1

for i in range(N):  ##배열 그래프화
    for j in range(M):
        if i-1 >= 0:
            graph[i * M + j].append(((i-1) * M + j,arr[i-1][j]))
        if j-1 >= 0:
            graph[i * M + j].append((i * M + j-1,arr[i][j-1]))
        if j+1 < M:
            graph[i * M + j].append((i * M + j+1,arr[i][j+1]))
        if i+1 < N:
            graph[i * M + j].append(((i+1) * M + j,arr[i+1][j]))

for i in range(N*M):    ##배열 시범출력
    for j in graph[i]:
        print(j, end=' ')
    print()


##for i in range(N*M):
##    print(graph[i][0][0])
            
def dfs(graph, v, visited):
    if visited[v] == 1:
        return
    visited[v] = 1

    print(v, end=' ')

    for i in graph[v]:
            dfs(graph, i[0], visited)

result = 0
for i in range(N*M):
    if visited[i] != 1:
        dfs(graph, i, visited)
        print()
        result += 1
print(result)

##
##입력 예시
"""
15 14
0 0 0 0 0 1 1 1 1 0 0 0 0 0
1 1 1 1 1 1 0 1 1 1 1 1 1 0
1 1 0 1 1 1 0 1 1 0 1 1 1 0
1 1 0 1 1 1 0 1 1 0 0 0 0 0
1 1 0 1 1 1 1 1 1 1 1 1 1 1
1 1 0 1 1 1 1 1 1 1 1 1 0 0
1 1 0 0 0 0 0 0 0 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 0 1 1
1 1 1 0 0 0 1 1 1 1 1 1 1 1
1 1 1 0 0 0 1 1 1 1 1 1 1 1
"""
##
##출력 해답 : 8
