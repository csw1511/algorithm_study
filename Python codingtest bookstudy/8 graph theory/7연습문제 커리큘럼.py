from collections import deque
n = int(input())
indegree = [0]*(n+1)

arr = [[]]
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

graph = [[] for i in range(n+1)]

studytime =[[]]

for i in range(1,n+1):
    studytime.append(arr[i][0])
    for j in range(1, len(arr[i])):
        if arr[i][j] != -1:
            graph[arr[i][j]].append((i, studytime[arr[i][j]]))
            indegree[i] += 1



def topology_sort():
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i[0]] -= 1
            if indegree[i[0]] == 0:
                q.append(i[0])
                studytime[i[0]] += studytime[now]
    
    for i in range(1,n+1):
        print(studytime[i], end='\n')
    
    

topology_sort()

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""