arr = list(map(int, input()))

result = arr[0]

for i in range(1, len(arr)):
    tmp1 = result + arr[i]
    tmp2 = result * arr[i]
    result = max(tmp1, tmp2)

print(result)




