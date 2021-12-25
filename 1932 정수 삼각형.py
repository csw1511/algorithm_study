n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

d = [[0 for i in range(500)] for j in range(500)]

d[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            d[i][j] = (d[i-1][j]+arr[i][j])
        elif j == len(arr[i])-1:
            d[i][j] = (d[i-1][len(arr[i-1])-1]+arr[i][j])
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + arr[i][j]
            
print(max(d[n-1]))
