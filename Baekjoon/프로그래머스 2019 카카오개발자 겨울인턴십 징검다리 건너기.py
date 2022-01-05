
def binsearch(low, high, stones, k):
    left = low
    right = high
    while (left <= right):
        mid = (left + right)//2
        temp = mid
        if temp < 0:
            temp = 0
        if Can_I_cross(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return left

def Can_I_cross(fixedstones, k, temp):
    count_0 = 0
    Can_cross_river = True
    for i in fixedstones:
        if i - temp <= 0:
            count_0 += 1
            if count_0 == k:
                return False
        if i - temp > 0:
            count_0 = 0
    return Can_cross_river
    
def solution(stones, k):
    answer = 0
    minor = 1
    maxim = 200000001
    answer = binsearch(minor, maxim, stones, k)
    
    return answer
