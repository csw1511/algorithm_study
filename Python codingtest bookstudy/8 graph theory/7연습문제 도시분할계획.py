def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

edges.sort()

result = 0

largestedge = 0

for edge in edges:
    cost, a, b = edge
    atmp = find_parent(parent, a)
    btmp = find_parent(parent, b)
    if atmp != btmp:
        union_parent(parent,a,b)
        result += cost
        largestedge = cost

print(result - largestedge)

"""
입력값
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
출력값
8

그래프에서 최소신장트리 2개 만드는 요령
1개 만들어진 최소신장트리에서 가장 비용이 큰 간선을 빼면 됨
"""



