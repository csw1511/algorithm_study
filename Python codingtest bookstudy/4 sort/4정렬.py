array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

##선택 정렬 : 매번 가장 작은것을 선택 O(n^2)
for i in range(len(array)):
    min_index = i ##가장 작은 원소의 인덱스
    for j in range(i + 1 , len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print('sellection sort:' , array)

##삽입 정렬 : 특정한 데이터를 적절한 위치에 삽입한다는 의미 O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):  ##0번째 인덱스는 그 자체로 정렬되었다고 생각
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print('insert sort:', array)

##퀵 정렬 : 피벗을 설정해 그걸 기준으로 배열을 좌우로 나누어 빠르게 정렬한다
##일반적으로 재귀형식을 이용해 구현하면 매우 편하다 O(NlogN)

##널리 사용되는 가장 직관적인 형태의 퀵정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -=1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print('quick sort general:',array)


##파이썬의 장점을 살린, 약간 비효율적이지만 구현이 간단한 형태의 퀵정렬 O(NlogN)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort1(array):
    if len(array)<=1:   ##리스트가 하나이하의 원소를 담았다면 정렬이 끝난것.종료
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [ x for x in tail if x <= pivot]    ##분할된 왼쪽부분
    right_side = [ x for x in tail if x > pivot]    ##분할된 오른쪽부분

    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)

print('quick sort python:', quick_sort1(array))


##계수 정렬. 모든 데이터가 양의 정수이고, 데이터중 최댓값이 K, 갯수 N일때 O(N+K)
##다만 데이터의 크기 범위가 제한되어 정수형태로 표현가능할때만 사용가능
##일반적으로 범위가 1,000,000을 넘지 않을때 효율적이며, 이는 모든 범위를 담을 수
##있는 크기의 리스트를 선언해야 하기 때문이다

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 1, 5, 2]
arr_minmax = [0]*(max(array)+1)
##arr의 범위(0~9)만큼의 크기를 갖는 0으로 초기화된 배열, max를 쓰면 바로 최댓값
##나온다. 개편하다.

for i in range(len(arr)):   ## arr의 배열에 각 숫자들이 몇번 등장했는지
    arr_minmax[arr[i]] +=  1    ##arr_minmax에 기록한다

for i in range(len(arr_minmax)): ##arr_mixmax에 기록된 횟수만큼 해당 인덱스를출력
    for j in range(arr_minmax[i]):
        print(i, end=' ')
print()
##때에 따라서 계수정렬은 매우 비효율적일수 있다. 데이터가 0과 999,999만 있다면?
##이럴때도 리스트의 크기를 100만이 되도록 선언해야 한다. 따라서 항상 사용할 수
##있는 정렬 알고리즘은 아니며, 동일한 값을 가지는 데이터가 여러 개 등장할때 적
##합하다. (ex)성적처리) 만약 데이터의 특성을 파악하기 어렵다면 퀵정렬을 사용하자


##기본 정렬 라이브러리 sorted()함수는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을
##기바으로 만들어졌는데, 일반적으로 퀵정렬보다 느리지만 최악의 경우에도 O(NlogN)
##을 보장한다는 특징이 있다. 이러한 sorted()함수는 리스트, 딕셔너리 자료형 등을
##입력받아서 정렬된 결과를 출력한다. 집합(set), 딕셔너리를 입력받아도 결과는
##리스트 자료형이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(array)
print(result)

##리스트가 하나 있을때 내부 원소를 바로 정렬할 수도 있는데, 이는 리스트 객체 내
##장 메소드인 sort()를 이용하는것이다. 별도의 정렬된 리스트가 반환되지 않고
##리스트의 내부원소가 바로 정렬된다

array.sort()
print(array)

##또한 sorted(), sort()를 이용할 땐 key 매개변수를 입력으로 받을 수 있다. key
##값으로는 하나의 함수가 들어가야 하며, 이는 정렬 기준이 된다.
##에를 들어 데이터가 튜플로 구성되어 있을 때, 각 데이터의 두 번재 원소를 기준
##으로 설정하는 경우는 다음처럼 작성가능하다. 또한 람다(lambda) 함수를 사용할
##수도 있다. 이는 부록에서 확인(lambda는 한번 써봤다)

array = [('바나나',2), ('사과', 5), ('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print(result)

##최악의 경우에도 O(NlogN)을 보장한다. 이들은 이미 잘 작성된 함수이므로 우리가 직
##접 퀵정렬을 구현할때보다도 더 효과적이다. 문제에서 별도 요구가 없다면
##단순히 정렬할때는 기본정렬 라이브러리 / 데이터 범위가 한정적이라면 계수정렬
##을 이용하자
##코딩테스트에서 정렬 알고리즘이 사용되는 경우를 일반적으로 3가지로 나눌 수 있다
##
##1. 정렬 라이브러리로 풀수 있는 문제 : 단순히 정렬 기법을 알고 있는지 물어보는
##문제로 기본 정렬 라이브러리의 사용법을 숙지하고 있다면 어렵지 않다
##2. 정렬 알고리즘의 원리에 대해서 물어보는 문제: 선택정렬, 삽입정렬, 퀵정렬
##등의 원리를 알고 있어야 문제를 풀 수 있다.
##3. 더 빠른 정렬이 필요한 문제: 퀵 정렬 기반의 정렬 기법으론 풀 수 없으며 계수
##정렬 등 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조
##적인 개선을 거쳐야 풀 수 있다.
