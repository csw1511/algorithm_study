row, col = map(int, input().split())

arr2d = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    arr2d[i] = list(map(int, input().split()))


minforcol = []
for i in range(row):
    minforcol.append(min(arr2d[i]))

print(max(minforcol))
