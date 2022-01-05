n, m = map(int, input().split())

arr1 = []

for i in range(n):
    arr1.append(list(map(int, input())))

arr2 = []

for i in range(n):
    arr2.append(list(map(int, input())))

compar = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j]:
            compar[i][j] = 1
        else:
            compar[i][j] = 2

print(compar)

        
