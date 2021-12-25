from collections import deque
INF = int(1e9)
n, k = map(int, input().split())

visited = [INF] * 100001

def bfs(visited, n, k):
    quee = deque()
    quee.append(n)
    visited[n] = 0
    temp = n
    while temp != k:
        temp = quee.popleft()
        if (temp-1) >=0 and (temp-1) <= 100000:
            if visited[temp-1] > visited[temp] + 1:
                visited[temp-1] = visited[temp] + 1
                quee.append(temp - 1)
                
        if (temp+1) >=0 and (temp+1) <= 100000:
            if visited[temp+1] > visited[temp] + 1:
                visited[temp+1] = visited[temp] + 1
                quee.append(temp + 1)
                
        if (temp*2) >=0 and (temp*2) <= 100000:
            if visited[temp*2] > visited[temp]:
                visited[temp*2] = visited[temp]
                quee.appendleft(temp * 2)
                
    return visited[temp]

print(bfs(visited, n, k))
