n = int(input())

arr = list(map(int, input().split()))

arr.sort()
count = 0
print(arr)

while arr:
    tmp = arr.pop()
    for i in range(tmp-1):
        arr.pop()
    count += 1


print(count)


