n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))


d = [0] * (n)


for i in range(n):
    if i == 0:
        d[i] = arr[i]
    elif i == 1:
        d[i] = arr[i] + arr[i-1]
    elif i == 2:
        d[i] = max(arr[i-1], arr[i-2]) + arr[i]
    else:
        d[i] = max(d[i-3]+arr[i-1], d[i-2]) + arr[i]
    
print(d[n-1])
