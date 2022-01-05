a, b = map(int, input().split())

result = 0
count = 0

while b != a:
    if (b-1) % 10 == 0:
        b = (b-1) // 10
        count += 1
    else:
        b = b/2
        count += 1
    if b<a:
        result = -1
        break
    
if result == -1:
    print(result)
else:
    result = count + 1
    print(result)
