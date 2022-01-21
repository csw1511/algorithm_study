x = int(input())

arr = [999999]*(x+1)



for i in range(x+1):
    if i == 0 or i == 1:
        arr[i] = 0
    
    if i * 5 <= x:
        if arr[i*5] > arr[i] + 1:
            arr[i*5] = arr[i] + 1

    if i * 3 <= x:
        if arr[i*3] > arr[i] + 1:
            arr[i*3] = arr[i] + 1
    
    if i * 2 <= x:
        if arr[i*2] > arr[i] + 1:
            arr[i*2] = arr[i] + 1
    
    if i + 1 <= x:
        if arr[i+1] > arr[i] + 1:
            arr[i+1] = arr[i] + 1


print(arr[x])
    
