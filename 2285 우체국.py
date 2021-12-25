n = int(input())
x = [0 for i in range(n)]
a = [0 for i in range(n)]

max_pos = 0

for i in range(n):
    x[i], a[i] = map(int, input().split())
    if x[i] > max_pos:
        max_pos = x[i]
    

#1. 완전탐색

def sum_of_path(n, mp):
    sum_ = abs(1 - x[0]) * a[0]
    for i in range(2, mp+1):
        tmp = sum_
        for j in range(n):
            tmp += (abs(i - x[j])) * a[j]
        sum_ = min(tmp, sum_)
    return sum_

print(sum_of_path(n, max_pos))

    
