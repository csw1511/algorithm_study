##인접 행렬(adjacency Matrix)
##2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
##연결되지 않은노드끼리는 무한의 비용을 설정. 대체로 99999999같이 걍 큰값 사용
INF = 999999999

graph = [
    [0, 7, 5],  ##0번 노드는 1과 7의 거리 / 2와 5의 거리
    [7, 0, INF],##1번 노드는 0과 7의 거리 / 2와 연결 안됨
    [5, INF, 0] ##2번 노드는 0과 5의 거리 / 1과 연결 안됨
]

print(graph)

##인접 리스트(adjacency List)
##모든 노드에 연결된 노드 정보를 차례대로 연결해 저장함.
##인접 리스트는 '연결 리스트'(Linked list) 자료구조를 이용하는데, C++나 자바는 별
##도의 연결리스트 기능을 위한 표준 라이브러리가 따로 있다.
##그러나 파이썬은 기본 자료형인 List자료형이 append()와 메소드를 제공하므로,
##전통적 프로그래밍 언어에서의 배열과 연결리스트의 기능을 모두 기본으로 제공한다.
##'파이썬의 인접 리스트를 이용해 그래프를 표현하고자 할때도 단순히 2차원 리스트를
##이용하면 된다'

graph = [[] for _ in range(3)]

graph[0].append((1,7))  ##0번 노드는 1과 7 길이의 간선으로 연결됨
graph[0].append((2,5))  ##0번 노드는 2와 5 길이의 간선으로 연결됨

graph[1].append((0,7))  ##1번 노드는 0과 7 길이의 간선으로 연결됨

graph[2].append((0,5))  ##2번 노드는 0과 5 길이의 간선으로 연결됨

print(graph)


##두 방식은 어떤 차이가 있는가? 1. 메모리 2. 속도 측면으로 살펴보자
##1. 메모리
##인접 행렬 : 모든 관계를 저장하므로 노드 개수가 많아질수록 메모리 낭비
##인접 리스트 : 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용
##2. 속도
##인접 행렬 : 특정한 두 노드가 연결되었는지에 대한 정보가 빠름. 바로 인덱스를 이
##용해 접근하면 되니까
##인접 리스트 : 인접 행렬 방식에 비해 해당 정보를 얻는데 느림. 연결된 데이터를
##하나하나 확인해야 되니까
##ex) 노드 1과 7의 연결여부를 확인
##인접 행렬 : graph[1][7] or graph[7][1] 으로 확인가능 - 반환값 1 or 간선길이
##인접 리스트 : 노드 1에 대한 인접 리스트를 앞에서 차례대로 7이 나올때까지 확인
##해야 함.
##>>> 그러므로 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우?
##인접 리스트가 인접 행렬보다 메모리 낭비가 적다.
