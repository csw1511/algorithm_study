from ctypes.wintypes import tagRECT


n, m = map(int, input().split())

arr = list(map(int, input().split()))


maxlen = max(arr)

lenarr = []

for i in range(maxlen+1):
    sumlen = 0
    for j in arr:
        if j >= i:
            sumlen += j - i
    lenarr.append(sumlen)


def binsear(arr, target, start, end):
    if start > end:
        return end;

    mid = (start+end)//2
    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binsear(arr, target, mid + 1, end)
    else:
        return binsear(arr, target, start, mid-1)

result = binsear(lenarr, m, 0, len(lenarr)-1)
print("절단기 높이: ", result)
print("손님이 가져가는 떡 길이: ", lenarr[result])
