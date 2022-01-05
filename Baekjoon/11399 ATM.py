n = int(input())

arr = [0]*n

arrPi= list(map(int, input().split()))

arrPi.sort()

for i in range(n):
    for j in range(i+1):
        arr[i] += arrPi[j]

result = 0

for i in range(n):
    result += arr[i]

print(result)
