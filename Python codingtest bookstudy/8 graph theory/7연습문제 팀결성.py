def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]

def union_team(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)

    if a > b:
        parent[a]=b
    else:
        parent[b]=a
    
n, m = map(int, input().split())

parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i


for _ in range(m):
    calc, a, b = map(int, input().split())
    if calc == 0:
        union_team(parent, a, b)
    elif calc == 1:
        atmp = find_team(parent, a)
        btmp = find_team(parent, b)
        if atmp == btmp:
            print("YES")
        elif atmp != btmp:
            print("NO")

"""
입력값
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
출력값
NO
NO
YES
"""