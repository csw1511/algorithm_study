##n = int(input())
##
##arrn = []
##
##first = 100001
##firstnode = 0
##
##for i in range(n):
##    aa = int(input())
##    if first > aa:
##        first = aa
##        firstnode = i
##    arrn.append(aa)
##
##
##matn = []
##for i in range(n):
##    matn.append(list(map(int, input().split())))
##
##
##t = []
##t.append(firstnode)
##result = arrn[firstnode]
##print(result)
##
##while len(t) != n:
##    tindex = []
##    for i in t:
##        tmparr = matn[i]
##        for j in t: #tmparr에서 이미 t에 들어있는 요소 100001로 만들기
##            tmparr[j] = 100001
##        tmpmin = 100001
##        tmpindex = 0
##        for i in range(len(tmparr)): # tmparr에서 최솟값과, 그 인덱스 찾기.
##            if tmpmin > tmparr[i]:
##                tmpmin = tmparr[i]
##                tmpindex = i
##        tindex.append((tmpmin, tmpindex))
##    tmp = min(tindex)
##    print(tmp)
##    t.append(tmp[1])
##    
##    result += min(tmp[0], arrn[tmp[1]])
##    print(result)
##
##print(t)
##print(result)
    
## 솔직히 내 풀이가 어디가 틀린지 잘 모르겠다.

n = int(input())

arrn = [0]

for i in range(n):
    aa = int(input())
    arrn.append(aa)
    
matn = []
matn.append(arrn)

for i in range(n):
    tmptmp = list(map(int, input().split()))
    tmptmp.insert(0,arrn[i+1])
    matn.append(tmptmp)

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

import sys

input = sys.stdin.readline

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v = n+1
e = sum(range(v))

parent = [0] * (v + 1)

edges = []
result = 0
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
# 모든 간선에 대한 정보를 입력받기
for i in range(v):
    for j in range(v):
        if i >= j:
            continue
        # 비용순으로 오름차순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((matn[i][j], i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)

#이 방법은 가상의 노드 0번을 만든 후, 기존의 각 노드가 가지는 '우물 파는'
#가중치를 0번 노드의 간선으로 치환한 후, 전체 그래프에 크루스칼 알고리즘을
#적용시켜 MST를 만듦으로써 해결하는 것이다.

## sample input
##8
##3
##3
##4
##5
##8
##2
##7
##9
##0 2 4 5 7 9 8 1
##2 0 4 8 7 6 1 2
##4 4 0 7 3 1 6 4
##5 8 7 0 7 2 4 9
##7 7 3 7 0 1 7 4
##9 6 1 2 1 0 5 4
##8 1 6 4 7 5 0 2
##1 2 4 9 4 4 2 0
