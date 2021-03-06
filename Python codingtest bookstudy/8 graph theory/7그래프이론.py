"""
이전에 배운내용 간단히 복습
우선순위 큐를 구현하는데 최소 힙/최대 힙이 쓰인다
우선순위 큐 만들기!
import heapq
q = []
heapq.heappush(q, (우선순위따질 값, 안따질 값))
우선순위를 따질 값을 튜플의 앞에 저장한다.
이렇게 만들면 기본적으로 우선순위 값이 작은 순서대로 큐에서 나오게 된다. 최소 힙이란 뜻이지
a, b = heapq.heappop(q)
이러면 튜플이 저 변수 a, b에 나뉘어서 저장됨. 이런식으로 큐에서 꺼냄!

최소 힙 = 트리임
트리 = 컴퓨터공학에선 방향 그래프


다익스트라 = 인접 리스트
플로이드 워셜 = 인접행렬

인접 리스트는 메모리를 덜 먹는대신 간선정보조회에 시간이 걸림
인접행렬은 메모리를 존나먹는대신 간선정보조회가 개빠름

노드개수가 적으면 플로이드워셜 때리면 되겠으나
노드와 간선 모두 많다면 다익스트라가 적절하겠다
"""


"""
서로소 집합 - 공통 원소가 없는 두 집합

서로소 집합 자료구조 - 소로소 부분집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조임
union과 find 이 2개의 연산으로 조작가능
union - 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
find - 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연사
서로소 집합 자료구조는 합집합union과 찾기find 연산으로 구성된다
그래서 union-find 자료구조라고 불리기도 함
두 집합이 서로소 관계인지 확인할수 있다 = 각 집합이 어떤 원소를 공통으로 가지고 있는지를 확인할 수 있다

자료구조 표현방법!
서로소 집합 자료구조 구현시에는 트리 자료구조를 이용하여 표현함. 
서로소 집합 정보가 주어졌을 때 트리 자료구조를 이요해 집합을 표현하는 서로소 집합 계산 알고리즘은
1. union 연산을 확인하여 서로 연결된 두 노드 A,B를 확인한다
    - A와 B의 루트 노드 A', B'를 각각 찾는다.
    - A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다)
2. 모든 union 연산을 처리할 때까지 1번과정을 반복한다.

실제로 구현할 땐 A'와 B'중에서 더 번호가 작은 원소가 부모노드가 되도록 구현하는 경우가 많다
A'가 1이고 B'가 3이면 B'가 A'를 가리키도록 ㅇㅇ
가리킨다 = 부모노드로 설정한다

예시!
[1,2,3,4,5,6]
4개의 union 연산
union 1,4 / union 2, 3 / union 2, 4 / union 5, 6

네개의 union연산은 각 1과 4는 같은 집합~ 이라는 의미를 가진다.
총 4개의 union연산이 존재함
이 4개 연산이 수행된 이후, 전체 원소들이 결과적으로 어떠한 형태의 부분집합으로 나누어질지 확인해보자

그림을 보면 빠르게 [1,2,3,4] 와 [5,6]이라는 두 집합으로 나뉘는것을 알 수 있다
노드 1 2 3 4가 같은 집합, 노드 5 6이 같은 집합인거임


서로소 집합 알고리즘 소스코드
"""

"""
def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v , e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end = ' ')
for i in range(1, v+1):
    print(find_parent(parent,i),end=' ')

print()

print('부모 테이블: ',end=' ')
for i in range(1, v+1):
    print(parent[i],end=' ')
"""

"""
이게 기본적인 방식이다. 그러나 이러면 find함수가 비효율적이다. 최악의 경우 find함수가 모든 노드를
다 확인하므로 시간복자볻가 O(V)이다
모든 원소가 루트노드 1을 가진다면 노드 5의 루트를 찾기 위해서는 5 4 3 2 1을 거쳐야 하는 그런경우가
있을수 있다. 이게 O(V)이지. 이러면 전체시간복잡도는 find/union연산개수가 M개일때 O(VM)이므로
매우 비효율적임
이러한 find함수는 간단한 과정으로 최적화가 가능하다
바로 '경로 압축' 이다!
경로 압축은 find를 재귀적으로 호출한 뒤 부모 테이블값을 갱신하는 기법이다.
그냥 부모테이블값을 find함수 내에서 실시간으로 갱신해주면 되는거임
이런식으로

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

재귀 들어갈 일이 있을때 바로바로 parent[x]에 갱신하고, 나중에 return할때 parent[x]자체를 
return하면 되니까 동작은 똑같음 이러면 각 노드에 대해 find함수를 호출한 이후 해당 노드의 루트노드
가 바로 부모노드가 된다. 즉 각 원소가 속한 집합이랍시고 출력한 값과, 부모테이블 값이 똑같아진다는 소리임

이 경우 시간복잡도는 O(V+M(1+log(2-M/V)V))라는 좆같이 복잡하네 아무튼 짧다
노드개수가 1000개이고 union/find연산이 100만번이라면 대략 1000만번의 연산이 필요한것
이러한 경로압축! 반드시 기억해두자. 이 버전으로 서로소집합을 기억해두자

서로소 집합을 활용한 사이클 판별
무방향 그래프 내에서의 사이클 판별시 사용할 수 있다
방향 그래프에서 사이클 여부는 DFS를 사용하면 되는데 이 책에선 다루지 않음

union연산은 그래프에서의 간선으로 표현될수 있다
따라서 간선을 하나씩 확인하면서 두 노드가 포함되어있는 집합을 합치는 과정을 반복하기만 해도
사이클 판별이 가능하다

1. 각 간선을 확인하며 두 노드의 루트노드를 확인한다
    - 루트노드가 서로 다르다면 두 노드에 대해 union연산을 수행한다
    - 루트노드가 서로 같다면 cycle이 발생한 것이다
2. 그래프에 포함되어있는 모든 간선에 대해 1번과정 반복

278쪽 그림 참조하기
그러니까 어떤 간선을 확인했는데 두 노드의 루트노드가 서로 같은경우 cycle이란것이다.
서로 다르면 union으로 루트노드를 찾고!

유의할 점 : 간선에 방향성이 없는 무방향 그래프에서만 가능하다

서로소 집합을 활용한 사이클 판별 소스코드
"""
"""
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v , e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print('cycle =', cycle)

"""

"""
신장 트리
그래프 알고리즘 문제로 자주 출제되는 문제유형
신장트리란? - 하나의 그래프가 있을때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

알고 있는거다!
이때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는것 << 트리의 성립조건이기도 함
그래서 이름을 신장트리라고 부르는거임


크루스칼 알고리즘 - 최소한의 비용을 갖는 신장트리 찾기
ex) 모든 도시를 연결할때 최소한의 비용으로 연결하기
크로스칼 알고리즘을 사용하면 가장 적은 비용으로 모든 노드를 연결가능함 - 기본적으로 그리디 알고리즘
모든 간선에 대해 정렬을 수행한 뒤 가장 거리가 짧은 간선부터 집합에 포함시킨다
이때 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않음

1. 간선데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재간선이 사이클을 발생시키는지 확인
    - 사이클이 발생하지 않는 경우 최소신장트리에 포함
    - 사이클이 발생하는 경우 최소신장트리에 포함시키지 않음
3. 모든 간선에 대해 2번의 과정 반복
여기서 어떤 간선이 사이클이 발생하는지 아는 방법 << 해당 간선이 연결하는 노드 두개가 이미 같은 
집합에 있는지 확인하기. 같은 집합이라면 앞서 서로소집합때처럼 사이클이 발생한것이겠지. 부모노드가
같은 상황일 것이다.

최소신장트리는 일종의 트리이므로, 신장트리에 포함되는 간선개수가 노드개수-1과 같다는 특징이 있다



크루스칼 알고리즘
"""

"""
def find_parent(parent,x):
    if parent[x] != x:
            parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v , e = map(int, input().split())
parent = [0]*(v+1)

# 모든 간선을 담아둘 리스트
edges = []
# 최종 비용을 담을 변수
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬하기 위해 cost를 튜플의 첫 원소로 집어넣음

#간선 정렬
edges.sort()

#간선을 비용 적은순서대로 하나씩 확인하며
for edge in edges:
    cost, a, b, = edge
    #만약 사이클이 발생하지 않는다면 집합에 포함
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
"""


"""
입력값
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
출력값
159
"""


"""
크루스칼 알고리즘은 간선개수가 E개일때 O(ElogE)의 시간복잡도를 가짐
왜냐면 가장 오래걸리는 작업이 정렬이고, E개의 데이터 정렬시간이 O(ElogE)이기 때문
서로소집합 알고리즘의 시간복잡도는 이에 비하면 너무 작으므로 무시함 ㅇㅇ
"""


"""
위상 정렬Topology Sort
정렬 알고리즘의 일종
위상 정렬 - 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할때 사용할 수 있는 알고리즘
- 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

진입차수 - 특정한 노드로 들어오는 간선의 개수를 의미함
위상정렬 수행하는 알고리즘
1. 진입차수가 0인 노드를 큐에 넣음
2. 큐가 빌때까지 다음과정 반복
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣음
이걸 이용하면 간단히 위상정렬 가능임;;

이때 모든 원소를 방문하기 전에 큐가 비어버리면 사이클이 발생한것이다
사이클이 있으면 사이클에 포함되어있는 원소중에서 어떠한 원소도 큐에 들어가지 못하기 때문임
생각해보니 당연함 ㅇㅇ 사이클에 포함되어있는 원소들은 전부 진입차수가 최소 1일테니까 큐에 못들어간다
다만 위상정렬문제에서는 사이클이 발생하지 않음을 명시하는경우가 더 많으므로 여기서 이는 고려하지
않는다

위에서 말한 과정을 수행하는 동안 큐에서 빠져나간 노드를 순서대로 출력하면 그것이 바로
위상정렬을 수행한 결과가 된다. 이 위상정렬의 답안은 여러가지가 될 수 있다.
한 단계에서 큐에 새롭게 들어가는 원소가 2개이상인 경우겠지 ㅇㅇ

위상정렬은 여기선 기본적으로 사이클이 없는 방향그래프를 방향에 거스르지 않는 방법으로 
정렬한다고 생각하자.

위상정렬 소스코드

"""

from collections import deque
v , e = map(int, input().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)

#각 노드에 연결된 간선정보를 담기 위한 연결리스트
graph = [[] for i in range(v+1)]

#간선정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    #진입차수 증가시키기
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()
print(indegree)

"""
입력값
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
출력값
1 2 5 3 6 4 7

위상정렬의 시간복잡도는 O(V+E)이다.
위상정렬을 수행할때 차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례로 제거하기
때문이다. 결과적으로 노드와 간선을 모두 확인하므로 O(V+E)이다
"""


"""
오늘 배운것

1. 서로소 집합(경로 압축 포함)
2. 서로소 집합을 이용한 사이클 판별(무방향 그래프에서만 유효)
3. 최소신장트리와 이를 찾기위한 크루스칼 알고리즘
4. 위상정렬(사이클 없는 방향그래프에서의 상황만 학습함)
"""