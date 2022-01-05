n = int(input())

arr = []

for i in range(n):
    temp = input().split()
    arr.append((temp[0], temp[1]))

##def setting(data):    ##일반적인 key에 함수이름 집어넣어서 이용하기
##    return data[1]
##
##arr2 = sorted(arr, key=setting)

##lambda 함수 이용하기

arr2 = sorted(arr, key=lambda student: student[1])
##lambda는 keyname인 student를 지정해, 그걸 arr의 원소로 보고 key의 기준을 지정한다

for i in arr2:
    print(i[0], end=' ')
