m, n = map(int, input().split())
arr = []
for i in range(m):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

maxcard = 0

for i in arr:
    tmp = min(i)
    if tmp > maxcard:
        maxcard = tmp

print(maxcard)