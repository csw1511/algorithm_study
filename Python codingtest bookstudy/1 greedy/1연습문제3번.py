n, k = map(int, input().split())

count = 0

while n != 1:
    if bool(n%k):
        n -= 1
        count += 1
    else:
        n /= k
        count += 1
print(count)
