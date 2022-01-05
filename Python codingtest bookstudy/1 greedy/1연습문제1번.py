n, m, k = map(int, input().split())

arr = list(map(int, input().split()))


sum = 0

first_Max = int(max(arr))

arr.remove(max(arr))

second_Max = int(max(arr))

##여기까지 가장 큰 수와 둘째로 큰 수 찾음

count_K = 0

for i in range(m):
    if count_K < k:
        sum += first_Max
        count_K += 1
    else:
        sum += second_Max
        count_K = 0

print(sum)
##
##위와 같이 for문을이용하여 푸는것도 좋으나, 반복되는 수열의 규칙(가장 큰 수를 K
##번더하고, 두번째로 큰 수를 1번 더하는게 반복되는)을 파악하여 수학적 연산을
##이용하면 for 반복문 없이 상수시간 안에 해결이 가능하다
