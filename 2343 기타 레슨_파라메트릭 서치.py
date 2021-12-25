n, k = map(int, input().split())

num_arr = []

num_arr = list(map(int, input().split()))

aver_low = 0
aver_high = 0
for i in num_arr:
    aver_high += i
aver_low = aver_high // k

def isitrun(num_arr, aver):
    count = 1
    sum_cut = 0
    for i in num_arr:   ##해당 평균값이 가능한지 체크 - 완성
        if i > aver:
            return False
        if sum_cut + i > aver:
            sum_cut = 0
            count += 1
        sum_cut += i

    if count <= k:
        return True
    else:
        return False
    

def binsearch(low, high, num_arr):
    left = low
    right = high

    while (left < right):
        mid = int((left + right)//2)
        if isitrun(num_arr, mid):
            right = mid
        else:
            left = mid + 1

    return int((left + right)//2)


print(binsearch(aver_low, aver_high, num_arr))
