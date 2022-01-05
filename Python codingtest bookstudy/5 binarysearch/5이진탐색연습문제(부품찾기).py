n = int(input())

narr = list(map(int, input().split()))

m = int(input())

marr = map(int, input().split())

narr.sort()

def binsearch(arr, left, right, target):    ##특정원소를 찾을때의 이진탐색 형태
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return True
        if arr[mid] < target :
            left = mid + 1
        else:
            right = mid - 1

    return False

for i in marr:
    print(binsearch(narr,0, len(narr)-1, i))
    
            
