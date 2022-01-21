##어떤 문제는 메모리 공간을 약간 더 사용하면 연산속도를 비약적으로 증가시킬
##수 있는 방법이 있다. 대표적 방법이 Dynamic programming(다이내믹 프로그래밍)
##이다.
##먼저 기본적 아이디어를 본 뒤 다-프의 두가지 방법(탑다운/바텀업)을 살펴보자
##또 이를 위해 자주 사용되는 메모이제이션 기법을 살펴보자
##
##다이나믹 프로그래밍을 사용할 수 있는 조건
##1. 큰 문제를 작은 문제로 나눌 수 있다.
##2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다
##
##피보나치 수열을 메모이제이션 방식으로 구해보자
##메모이제이션 : 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면
##메모한 결과를 그대로 가져오는 기법. 값을 저장하는 방법이므로 캐싱(caching)이라
##고도 한다
##구현방법은 단순하다. 한번 구한 정보를 리스트에 저장하기만 하면 됨
##다이내믹 프로그래밍을 재귀적으로 수행하다 같은 정보가 필요할 때는 이미 구한
##정답을 그대로 리스트에서 가져오면 된다

##메모이제이션 기법을 위한 결과 저장 리스트
d = [0]*100
##메모이제이션을 활용한 피보나치 재귀함수
def fibbo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibbo(n-1) + fibbo(n-2)
    return d[n]

print(fibbo(99))

##정리하자면 다이나믹 프로그래밍이란 큰 문제를 작게 나누고, 같은 문제라면 한 번
##씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법이다.
##사실 큰 문제를 작게 나누는 방법은 퀵 정렬에서도 소개한 적이 있는데, 퀵정렬은
##정렬을 수행할 때 정렬할 리스트를 분할하며 전체적으로 정렬이 될 수 있도록
##한다. 이는 '분할 정복 알고리즘'으로 분류된다. 다이나믹 프로그래밍과 분할 정복의
##차이점은 다이나믹 프로그래밍은 문제들이 서로 영향을 미치고 있다는 점이다
##퀵 정렬을 예로 들면, 한번 기준원소가 자리를 변경해 자리잡게 되면 그 기준원소의
##위치는 더이상 바뀌지 않고 그 피벗값을 다시 처리하는 부분문제는 존재하지 않는다.
##반면 다이나믹 프로그래밍은 한번 해결했던 문제를 다시금 해결한다는 점이 특징이다.
##그렇기 때문에 이미 해결된 부분문제에 대한 답을 저장해놓고, 이 문제는 이미 해결된
##것이니까 다시 해결할 필요가 없다고 반환하는 것이다.
##또한 일반적으로 재귀함수보다 반복문을 사용하는 다이나믹 프로그래밍이 더 성능이
##좋은데, 이는 재귀는 이미 해결된 작은 문제의 값을 리스트에서 가져올때도 어쨌든
##호출은 해야 하기 때문에 오버헤드가 발생할 수 있기 때문이다.
##
##이처럼 재귀함수를 이용하여 다이나믹 프로그래밍 소스코드를 작성하는 방법을
##큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 탑다운 방식이라고 말한다.
##반면 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근
##답을 도출한다고 하여 바텀업 방식이라고 말한다. 피보나치 수열 문제를 아래에서 위
##로 올라가는 바텀업 방식으로 풀면 다음과 같다.

d = [0]*100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])

##탑다운 - 하향식 / 바텀업 - 상향식이라고도 한다. 다이나믹 프로그래밍의 전형적인
##형태는 바텀업 방식이다. 바텀업에서 사용되는 결과 저장용 리스트는 'DP테이블'
##이라고 부르며, 메모이제이션은 탑다운 방식에 국한되어 사용되는 표현이다.
##다이나믹 프로그래밍과 메모이제이션의 개념을 혼용해 사용하는 경우도 있는데, 엄밀
##히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해놓는 넓은 개념을
##의미하므로, 다이나믹 프로그래밍과는 별도의 개념이다. 한번 계산된 결과를 어
##딘가에 담아놓기만 하고 다이나믹 프로그래밍을 위하 활용하지 않을수도 있는것이다.
##또한 앞서 수열은 배열/리스트로 표현할 수 있다고 했는데, 메모이제이션은 때에
##따라 다른 자료형, 예를 들어 사전(dict)자료형을 이용할 수도 있다. 사전 자료형은
##수열처럼 연속적이지 않은 경우에 유용한데 예를 들어 a(n)을 게산하고자 할때
##a(0) ~ a(n-1) 모두가 아닌 일부의 작은 문제에 대한 해답만 필요한 경우가 존재할
##수 있다. 이럴 때는 사전 자료형이 효과적이다.
##다이나믹 프로그래밍을 이용해 피보나치를 풀었던 방법을 잘 알아두자. 다른
##다이나믹 형식의 문제에 접근하는 방법 또한 떠올릴 수 있을 것이다. 물론 3차원 리스
##트를 이요해야 하는 복잡한 난이도의 문제가 출제될 수도 있다. 이런 문제는
##최단경로 - 플로이드 워셜 알고리즘에서 알아보다.
##하지만 코테에서 다이내믹 문제는 대체로 간단한 형태이다. 기초만 잘 다지자 기초만
##첫 단계는 문제가 다이내믹 형식임을 파악하는 것이다. 특정 문제를 완전탐색으로
##접근했을 때 시간이 매우오래걸리면 다이나믹을 적용할 수 있는지, 해결하고자 하는
##부분 문제들의 중복여부는 어떤지 살펴보자
##일단 단순히 재귛마수로 비효율적 프로그램을 작성한 뒤(탑다운) 작은 문제에서 구한
##답이 큰 문제에서도 그대로 사용될 수 있으면 바로여기서 '메모이제이션' 딱 적용해서
##코드를 개선하는거도 좋다.
##또한 가능하다면 재귀함수보단 바텀업 방식 구현이 좋다. 시스템상 재귀함수 스택크기가
##한정되어 있을수 있기 때문이다. 실제로 앞에서 피보나치 재귀에서 오천번째 이상
##큰 피보나치를 구하려고 하면 'recursion depth'(재귀함수 깊이)와 관련된 오류가 발
##생할 수 있다. 이 경우 sys라이브러리의 'setrecursionlimit()'함수를 호출하여
##재귀제한을 완화할 수는 있는데 걍 바텀업으로 짜면 이딴고민 안해도됨
