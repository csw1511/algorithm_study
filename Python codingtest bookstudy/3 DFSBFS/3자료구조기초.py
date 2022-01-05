##Stack

stack = []      ##스택 사용에 별도 라이브러리 필요없다. 그냥 append와 pop으로 구현
stack.append(5)
stack.append(2)
stack.append(3) 
stack.append(7) ##5 2 3 7
stack.pop()     ##5 2 3
stack.append(1) ##5 2 3 1
stack.append(4) ##5 2 3 1 4
stack.pop()     ##5 2 3 1

print(stack)    ##스택출력
print(stack[::-1])##스택거꾸로출력


##Queue

from collections import deque
##큐를 구현하기 위한 조건. collections 라이브러리에서 deque 함수만 import 시켰다
##deque 는 스택과 큐의 장점을 모두 채택한 것. 데이터를 넣고빼는 속도가 list보다
##효율적이며 queue 라이브러리를 이용하는것보다 간단하다.
queue = deque() ##큐 생성. deque 함수를 queue 변수에 대입

queue.append(5) 
queue.append(2) 
queue.append(3)
queue.append(7) ##5 2 3 7
queue.popleft() ##2 3 7
queue.append(1) ##2 3 7 1
queue.append(4) ##2 3 7 1 4
queue.popleft() ##3 7 1 4

print(queue)    ##큐 출력
queue.reverse() ##큐는 list가 아니므로 전용함수로 뒤집는다
print(queue)    ##뒤집어진 큐 출력
print(list(queue))##큐를 리스트 화 시킴
##queue.popright()  이따위 함수는 없다



##재귀 한번 짚기
def recursive_fuction(i):
    if i == 10:
        return
    print( i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_fuction(i +1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_fuction(1)
## 출력을 보고 알 수 있듯이 재귀함수 수행은 '스택'ㅡ을 이용한다. 가장 마지막에
##호출된 함수가 먼저 수행을 끝내야 그 앞의 함수호출이 종료될 수 있기 때문이다.
##재귀 함수는 내부적으로 스택 자료구조와 동일하다는 것만 기억하자
##따라서 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀함수를 이용해 간편히
##구현할 수 있다. 대표적으로 DFS가 있다.

##다음은 팩토리얼을 각각 반복과 재귀를 이용해 구현한 예시
def facto_iter(n):  ##반복을 이용한 팩토리얼
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def facto_recur(n):
    if n <= 1:
        return 1    ##재귀함수의 종료조건
    result = facto_recur(n-1) * n
    return result

print('반복 구현:', facto_iter(5))
print('재귀 구현:', facto_recur(5))

##재귀의 장점은?
##구현이 간단하다. 수학의 점화식(재귀식)을 그대로 소스코드로 옮길 수 있기 때문.
##이는 후에 배울 다이나믹 프로그래밍과 연관이 크므로 중요하다ㅡㅡ''점화식''
