n, m = map(int,input().split())

arr = list(map(int,input().split()))

arrcount = []

for i in range(1, m+1):
    arrcount.append(arr.count(i))

result = n*(n-1)//2

for i in arrcount:
    if i > 1:
        result -= i*(i-1)//2

print(result)



