n = int(input())

d = [10000000] * (n+1)

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

def startpoint(a, arr):
    sum = arr[0][a]
    
    for i in range(1, n):
        temp = 0
        if a == 0:
            temp = min(arr[i][1], arr[i][2])
        elif a == 1:
            temp = min(arr[i][0], arr[i][2])
        elif a == 2:
            temp = min(arr[i][1], arr[i][2])
        for j in range(3):
            if temp == arr[i][j]:
                a = j

        
