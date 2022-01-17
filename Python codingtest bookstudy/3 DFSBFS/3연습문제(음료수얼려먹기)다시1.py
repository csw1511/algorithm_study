"""
입력된 그래프가 2차원 배열이므로 이에 맞게 DFS 개조를 거침
dx dy를 사용하여 상하좌우 0이 있다면 이를 연결된 노드로 취급하여 DFS를 실행한다
"""
def dfs(visited, v1, v2):
    visited[v1][v2] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    
    for i in range(4):
        nextv1 = v1 + dx[i]
        nextv2 = v2 + dy[i]
        if nextv1 < n and nextv1 >= 0 and nextv2 < m and nextv2 >= 0:
            if visited[nextv1][nextv2] == 0:
                dfs(visited,nextv1, nextv2)
        else:
            continue

n, m = map(int, input().split())

visited = []

for i in range(n):
    tmp = list(map(int,input()))
    visited.append(tmp)


##생성된 총 아이스크림 개수를 구하는 변수
count = 0

##모든 배열 인덱스를 돌며 만약 해당부분이 0일시 dfs 실행. dfs실행횟수가 곧 아이스크림 갯수이다
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dfs(visited,i,j)
            count += 1


print(count)

"""
입력예시 1
4 5
00110
00011
11111
00000
"""


"""
입력예시 2
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""