n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

max1 = arr.pop()
max2 = arr.pop()

result = 0

count = k
while m != 0:
    if count != 0:
        result += max1
    if count == 0:
        result += max2
        count = k
    count -= 1
    m -= 1

print(result)
