n = int(input())

d = [0] * 12

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 12):
    count = 0
##    if i-3 <= 3:
##        count += 1
##    if i-2 <= 3:
##        count += 1
##    if i-1 <= 3:
##        count += 1

    d[i] = d[i-1] + d[i-2] + d[i-3] + count

for i in range(n):
    temp = int(input())
    print(d[temp])
