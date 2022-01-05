##BFS : 너비우선탐색(Breadth-First Search)
##가까운 노드부터 탐색함. 선입선출( FIFO ) 방식인 큐(Queue) 를 이용하는것이 정석.
##인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스레 먼저 들어온
##것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행한다
##1. 탐색 시작 노드를 큐에 삽입하고 방문처리
##2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 '모두'
##큐에 삽입하고 방문처리
##3. 2번의 과정을 끝까지 반복

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:    ##이는 큐가 빌 때까지 반복함을 의미한다
            v = queue.popleft() ##큐에서 하나의 원소를 뽑아 출력. popleft함수는
                                ##이렇게 호출하면 queue에 영향을 미친다
            print(v, end=' ')

            for i in graph[v]:  ##처음은 시작노드가 v가 된다.
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True    ##정말 이렇게만 하면 되나?
##이것이 의미하는 바는? 여기 for문은 graph의 v노드에 연결된 모든 노드를 queue
##에 집어넣고 방문처리함을 의미한다. 이 for가 끝나면? 이를 둘러싼 while문으로
##돌아간다. 아직 queue가 비지 않았으므로 queue에서 값을 뽑고 다시 그 값을 v
##로 만들어 해당 노드(v)에 연결된 모든 노드를 다시 queue에 집어넣고 방문처리
##한다. 언젠가 모든 노드가 방문처리가 됨으로써 queue는 텅 빌 것이고 while문도
##끝날 것이다.

        

visited = [False]*9

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

bfs(graph, 1, visited)

##일반적으로 실제 수행시간은 DFS보다 좋은편이다
