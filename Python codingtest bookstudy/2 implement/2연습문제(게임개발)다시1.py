row, col = map(int, input().split())

set4look = [(-1, 0),(0, -1),(1, 0),(0, 1)]## 각각 북 서 남 동

charx, chary, charlook = map(int, input().split())
charx += 1
chary += 1
if charlook == 3:
    charlook = 1
elif charlook == 1:
    charlook = 3

arr = [[1 for i in range(col+2)] for j in range(row+2)]
## row x col 크기의 배열 생성

for i in range(row):
    temp = list(map(int, input().split()))
    for j in range(col):
        arr[i+1][j+1] = temp[j]
##입력끝


def trav(x, y, l):
    listtotrav = []
    listtotrav.append(arr[x-1][y])
    listtotrav.append(arr[x][y-1])
    listtotrav.append(arr[x+1][y])
    listtotrav.append(arr[x][y+1])
    print(listoftrav)
    for i in range(4):
        if listtotrav[i] == 0:
            charlook = i
            charx += set4look[i][1]
            chary += set4look[i][0]
            break

## 실패
    
